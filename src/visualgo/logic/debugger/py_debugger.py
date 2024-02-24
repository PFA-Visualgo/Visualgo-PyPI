from typing import Callable, TypeVar

from .debugger_callbacks import DebuggerCallbacksInterface

T = TypeVar("T")


class PyDebugger:
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
