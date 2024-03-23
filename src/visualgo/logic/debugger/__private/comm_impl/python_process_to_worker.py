import os
import signal
from typing import Any, Callable

from ..comm_api.to_worker import ToWorker
from .python_process_from_worker import PythonProcessFromWorker
from multiprocessing import Process, Pipe


def _wrapper_task(task, pipe_conn, parent_pid):
    from ..comm_api.from_worker import set_implementation
    impl = PythonProcessFromWorker(pipe_conn, parent_pid)
    set_implementation(impl)
    impl.send_message("INITIALIZED", None)
    task()


def signal_handler(message_handler, conn_main, sig, frame):
    mes_id, mes_data = conn_main.recv()
    message_handler(mes_id, mes_data)


class PythonProcessToWorker(ToWorker):
    def __init__(self, task: Callable[[], None], message_handler: Callable[[str, Any], None]):
        self.message_value: [str, Any] = None
        self.task: Callable[[], None] = task
        self.conn_main, conn_worker = Pipe()
        self.worker_process = Process(target=_wrapper_task, args=(task, conn_worker, os.getpid()))
        self.message_handler: Callable[[str, Any], None] = message_handler
        signal.signal(signal.SIGUSR1,
                      lambda sig, frame: signal_handler(self.message_handler, self.conn_main, sig, frame))

    def set_message_handler(self, message_handler: Callable[[str, Any], None]):
        self.message_handler = message_handler

    def send_message(self, mes_id: str, mes_data: Any):
        self.conn_main.send((mes_id, mes_data))

    def start_worker(self):
        self.worker_process.start()

    def interrupt_worker(self):
        self.worker_process.terminate()
