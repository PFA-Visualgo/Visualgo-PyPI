from abc import ABC, abstractmethod

from .types import TransferVariables
from ..types import Statistics, CodeError


class UICallbacksInterface(ABC):
    """
    Interface for the UI Callbacks in order to communicate with the UI.

    :demand: F.1.7
    """

    @abstractmethod
    def set_current_line(self, line: int) -> None:
        """
        Update the UI to show that the last executed line is `line`.

        :param variables: TransferVariables
        :return: None
        """
        pass

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

        :demand: F.1.5
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