from typing import TypeVar

from ..controller_callbacks import ControllerCallbacksInterface
from .debugger import AbstractDebugger

T = TypeVar("T")


class PyAbstractDebugger(AbstractDebugger):
    """
    Python language support of the DebuggerInterface.
    """

    def __init__(self, callbacks: ControllerCallbacksInterface) -> None:
        super().__init__(callbacks)

    def stop(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def set_code(self, code: str) -> None:
        raise NotImplementedError("Method not implemented yet")

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        raise NotImplementedError("Method not implemented yet")

    def del_breakpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not implemented yet")

    def backward_step(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def forward_step(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def forward_next(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def do_continue(self) -> None:
        raise NotImplementedError("Method not implemented yet")
