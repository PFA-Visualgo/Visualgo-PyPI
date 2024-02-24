from abc import ABC, abstractmethod

from ..stats import Stats


class TransferVars:
    pass


class UICallbacksInterface(ABC):

    @abstractmethod
    def update_variables(self, vars: TransferVars) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_statistics(self, stats: Stats) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_error(self, message: str) -> None:
        raise NotImplementedError
