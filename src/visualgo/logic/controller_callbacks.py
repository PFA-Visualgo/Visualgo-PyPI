from abc import ABC, abstractmethod

from .debugger.types import DebugContext
from .types import CodeError


class ControllerCallbacksInterface(ABC):
    """
    Interface so that the debugger can call when it has finished an action asked by the controller.
    """

    @abstractmethod
    def backward_step_done(self, context: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the backward_step() has been done in the debugger.

        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def forward_step_done(self, context: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the forward_step() has been done in the debugger.

        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def forward_next_done(self, context: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the forward_next() has been done in the debugger.

        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def do_continue_done(self, context: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the do_continue() has been done in the debugger.

        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def end_of_code_reached(self, context: DebugContext, line_number: int) -> None:
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
        Show an error in the visualisation when the debugger has found one in the client code.

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
