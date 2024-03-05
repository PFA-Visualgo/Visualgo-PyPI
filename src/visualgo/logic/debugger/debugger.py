from abc import ABC, abstractmethod
from typing import Callable, TypeVar

from .debug_types import DebugContext

T = TypeVar("T")

class DebuggerInterface(ABC):
    """
    Interface for the Debugger class.
    """

    @abstractmethod
    def add_breakpoint(self, line_number: int, cond: Callable[[T],bool]) -> None:
        """
        Add a new breakpoint at the given `line_number` with a condition `cond`.
        :param line_number: int
        :param cond: Callable[[T],bool]
        :return: None
        """
        pass

    @abstractmethod
    def forward_step_into(self) -> None:
        """
        Make a forward 'step into' the execution, it will enter in the function if it is a function call.
        :return: None
        """
        pass

    @abstractmethod
    def forward_step(self) -> None:
        """
        Make a forward 'step' in the execution.
        :return: None
        """
        pass

    @abstractmethod
    def backward_step(self) -> None:
        """
        Make a backward 'step' in the execution.
        :return: None
        """
        pass

    @abstractmethod
    def do_continue(self) -> None:
        """
        Continue the execution until the next breakpoint.
        :return: None
        """
        pass

class DebuggerCallbacksInterface(ABC):
    """
    Interface for the DebuggerCallbacks class.
    """

    @abstractmethod
    def backward_step_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def forward_step_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def forward_step_into_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def backward_step_into_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def continue_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def end_of_code_reached(self, vars: DebugContext, line_number: int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

