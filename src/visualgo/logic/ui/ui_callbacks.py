from abc import ABC, abstractmethod

from .types import TransferVariables
from ..types import Statistics, CodeError


class UICallbacksInterface(ABC):
    """
    Interface for the UI Callbacks in order to communicate with the UI.
    """

    @abstractmethod
    def update_variables(self, variables: TransferVariables) -> None:
        """
        Updates the variables in the UI with the given `variables`.
        :param variables: TransferVariables
        :return: None
        """
        pass

    @abstractmethod
    def update_statistics(self, statistics: Statistics) -> None:
        """
        Updates the statistics in the UI with the given `statistics`.
        :param statistics: Statistics
        :return: None
        """
        pass

    @abstractmethod
    def show_error(self, error: CodeError) -> None:
        """
        Shows the error in the UI with the given `error`.
        :param error: CodeError
        :return: None
        """
        pass

    @abstractmethod
    def get_code(self) -> str:
        """
        Returns the user code from the UI.
        :return: str
        """
        pass

# Creates a class of UICallbacksInterface
# class UICallbacks(UICallbacksInterface):
#     ...
