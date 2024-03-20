import ctypes
import inspect
import os
import time

from ..comm_api import to_worker
from .python_from_worker import PythonFromWorker
import threading
from typing import Callable, Any
from .python_shared_worker_data import set_impl

class InterruptedThreadException(Exception):
    pass

def _async_raise(tid, exctype):
    """Raises an exception in the threads with id tid"""
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
                                                     ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class ThreadWithExc(threading.Thread):
    """A thread class that supports raising an exception in the thread from
       another thread.
    """

    def _get_my_tid(self):
        """determines this (self's) thread id

        CAREFUL: this function is executed in the context of the caller
        thread, to get the identity of the thread represented by this
        instance.
        """
        if not self.is_alive():  # Note: self.isAlive() on older version of Python
            raise threading.ThreadError("the thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        raise AssertionError("could not determine the thread's id")

    def raise_exc(self, exctype):
        """Raises the given exception type in the context of this thread.

        If the thread is busy in a system call (time.sleep(),
        socket.accept(), ...), the exception is simply ignored.

        If you are sure that your exception should terminate the thread,
        one way to ensure that it works is:

            t = ThreadWithExc( ... )
            ...
            t.raise_exc( SomeException )
            while t.isAlive():
                time.sleep( 0.1 )
                t.raise_exc( SomeException )

        If the exception is to be caught by the thread, you need a way to
        check that your thread has caught it.

        CAREFUL: this function is executed in the context of the
        caller thread, to raise an exception in the context of the
        thread represented by this instance.
        """
        _async_raise(self._get_my_tid(), exctype)


class PythonToWorker(to_worker.ToWorker):
    def __init__(self, task: Callable[[], None], message_handler: Callable[[str, Any], None]):
        self.ev: threading.Event = threading.Event()
        self.message_value: [str, Any] = None
        self.task: Callable[[], None] = task
        self.worker_thread = ThreadWithExc(target=self.wrapper_task)
        self.message_handler: Callable[[str, Any], None] = message_handler
        set_impl(self)
        self.worker_thread.start()

    def wrapper_task(self):
        from ..comm_api.from_worker import set_implementation
        impl = PythonFromWorker()
        set_implementation(impl)
        try:
            self.task()
        except InterruptedThreadException:
            impl.send_message("INTERRUPTED", None)
            print("\nThread has been interrupted")
            time.sleep(0)

    def set_message_handler(self, message_handler: Callable[[str, Any], None]):
        self.message_handler = message_handler

    def send_message(self, mes_id: str, mes_data: Any):
        self.message_value = (mes_id, mes_data)
        self.ev.set()

    def interrupt_worker(self):
        self.worker_thread.raise_exc(InterruptedThreadException)
