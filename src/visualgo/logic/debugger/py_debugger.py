from typing import TypeVar

from ..controller_callbacks import ControllerCallbacksInterface
from .debugger import DebuggerInterface

T = TypeVar("T")


class PyDebugger(DebuggerInterface):
    """
    Python language support of the DebuggerInterface.
    """

    def __init__(self, callbacks: ControllerCallbacksInterface) -> None:
        raise NotImplementedError("Method not implemented yet")

    def set_code(self, code: str) -> None:
        raise NotImplementedError("Method not implemented yet")

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        raise NotImplementedError("Method not implemented yet")

    def backward_step(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def forward_step(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def step_into(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def do_continue(self) -> None:
        raise NotImplementedError("Method not implemented yet")
