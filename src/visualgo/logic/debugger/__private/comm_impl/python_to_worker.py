from ..comm_api import to_worker
from .python_from_worker import PythonFromWorker
import threading
from typing import Callable, Any
from .python_shared_worker_data import set_impl


class PythonToWorker(to_worker.ToWorker):
    def __init__(self, task: Callable[[], None], message_handler: Callable[[str, Any], None]):
        self.ev: threading.Event = threading.Event()
        self.message_value: [str, Any] = None
        self.task: Callable[[], None] = task
        self.worker_thread: threading.Thread = threading.Thread(target=self.wrapper_task)
        self.message_handler: Callable[[str, Any], None] = message_handler
        set_impl(self)
        self.worker_thread.start()

    def wrapper_task(self):
        from ..comm_api.from_worker import set_implementation
        set_implementation(PythonFromWorker())
        self.task()

    def set_message_handler(self, message_handler: Callable[[str, Any], None]):
        self.message_handler = message_handler

    def send_message(self, mes_id: str, mes_data: Any):
        self.message_value = (mes_id, mes_data)
        self.ev.set()

    def interrupt_worker(self):
        raise NotImplementedError("Method not implemented")
