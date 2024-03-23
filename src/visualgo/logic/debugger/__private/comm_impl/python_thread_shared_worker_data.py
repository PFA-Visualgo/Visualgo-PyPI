import os
import threading
import typing
from typing import Callable, Any
import signal

if typing.TYPE_CHECKING:
    from .python_thread_to_worker import PythonToWorker
my_impl: "PythonToWorker"
worker_mess_val: [str, Any]


def signal_handler(signum, frame) -> None:
    my_impl.message_handler(*worker_mess_val)
    # os.sched_yield()


def set_impl(impl: "PythonToWorker") -> None:
    global my_impl
    my_impl = impl

    signal.signal(signal.SIGUSR1, signal_handler)


def get_main_message_value():
    return my_impl.message_value


def get_event() -> threading.Event:
    return my_impl.ev


def get_message_handler() -> Callable[[str, Any], None]:
    return my_impl.message_handler


def set_worker_message_value(mes_id: str, data):
    global worker_mess_val
    worker_mess_val = (mes_id, data)
