from abc import ABC, abstractmethod
from typing import Callable, Any


class ToWorker(ABC):

    @abstractmethod
    def set_message_handler(self, message_handler: Callable[[str, Any], None]):
        ...

    @abstractmethod
    def send_message(self, mes_id: str, mes_data: Any):
        ...

    @abstractmethod
    def interrupt_worker(self):
        ...


to_worker_impl: ToWorker


def set_implementation(impl: ToWorker):
    global to_worker_impl
    to_worker_impl = impl


def get_implementation():
    return to_worker_impl
