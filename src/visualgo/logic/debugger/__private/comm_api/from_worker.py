from abc import ABC, abstractmethod
from typing import Any, Callable


class FromWorker(ABC):
    @abstractmethod
    def send_message(self, mes_id: str, data: Any):
        ...

    @abstractmethod
    def wait_for_main_message(self) -> (str, Any):
        ...


__to_worker_impl: FromWorker


def set_implementation(impl: FromWorker):
    global __to_worker_impl
    __to_worker_impl = impl


def get_implementation():
    return __to_worker_impl
