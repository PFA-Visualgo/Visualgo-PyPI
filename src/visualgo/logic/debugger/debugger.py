from abc import ABC, abstractmethod
from typing import TypeVar

from .. import ControllerCallbacksInterface

T = TypeVar("T")


class DebuggerInterface(ABC):
    """
    Interface for the Debugger class.
    """

    @abstractmethod
    def __init__(self, callbacks: ControllerCallbacksInterface) -> None:
        """
        Constructor of the Debugger class. It will receive the callbacks to call when the debugger has finished an action.

        :param controller_callbacks: ControllerCallbacksInterface
        """
        pass

    @abstractmethod
    def set_code(self, code: str) -> None:
        """
        Set or reset the code to be executed.

        :param code: str
        :return: None
        """
        pass

    @abstractmethod
    def add_breakpoint(self, line_number: int, cond: str) -> None:
        """
        Add a new breakpoint at the given `line_number` with a condition `cond`.

        :param line_number: int
        :param cond: str
        :return: None
        """
        pass

    @abstractmethod
    def step_into(self) -> None:
        """
        Make a forward 'step into' the execution, it will enter in the function if it is a function call.

        :call: callbacks.step_into_done(context, line_number)
        :return: None
        """
        pass

    @abstractmethod
    def forward_step(self) -> None:
        """
        Make a forward 'step' in the execution.

        :call: callbacks.forward_step_done(context, line_number)
        :return: None
        """
        pass

    @abstractmethod
    def backward_step(self) -> None:
        """
        Make a backward 'step' in the execution.

        :call: callbacks.backward_step_done(context, line_number)
        :return: None
        """
        pass

    @abstractmethod
    def do_continue(self) -> None:
        """
        Continue the execution until the next breakpoint.

        :call: callbacks.do_continue_done(context, line_number)
        :return: None
        """
        pass
