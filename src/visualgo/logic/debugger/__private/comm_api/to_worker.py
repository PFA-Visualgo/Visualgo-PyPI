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
    def start_worker(self):
        ...

    @abstractmethod
    def interrupt_worker(self):
        ...


__to_worker_impl: ToWorker


def set_implementation(impl: ToWorker):
    global __to_worker_impl
    __to_worker_impl = impl


def get_implementation():
    return __to_worker_impl
