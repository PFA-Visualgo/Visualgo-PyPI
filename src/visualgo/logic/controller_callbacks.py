from abc import ABC, abstractmethod

from .debugger.types import DebugContext
from .types import CodeError


class ControllerCallbacksInterface(ABC):
    """
    Interface so that the debugger can call when it has finished an action asked by the controller.
    """

    @abstractmethod
    def execution_paused(self, frames: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the debugger has finished executing code and is awaiting
        further instructions. Occurs on steps, next and continues.
        :param context:
        :param line_number:
        :return:
        """
        ...

    @abstractmethod
    def execution_done(self, frames: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the end of the code has been reached in the debugger.

        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def on_error(self, error: CodeError) -> None:
        """
        Show an error in the visualisation when the debugged code throws an un-caught exception

        :param error: CodeError
        :return: None
        """
        pass

    @abstractmethod
    def on_message(self, message: str) -> None:
        """
        Show a message in the visualisation when one is printed in the client code by the debugger.

        :param message: str
        :return: None
        """
        pass
