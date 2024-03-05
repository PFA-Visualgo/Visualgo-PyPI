from typing import Callable, TypeVar

from .debugger import DebuggerCallbacksInterface
from .debugger import DebuggerInterface

T = TypeVar("T")

class PyDebugger(DebuggerInterface):
    """
    Python language support of the DebuggerInterface.
    """

    def __init__(
            self, code: str, callbacks: DebuggerCallbacksInterface) -> None:
        pass

    def add_breakpoint(
            self, line_number: int, cond: Callable[[T],
                                                   bool]) -> None:
        pass

    def backward_step(self) -> None:
        pass

    def forward_step(self) -> None:
        pass

    def step_into(self) -> None:
        pass

    def do_continue(self) -> None:
        pass
