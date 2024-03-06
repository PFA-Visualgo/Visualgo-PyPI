from typing import TypeVar

from ..controller_callbacks import ControllerCallbacksInterface
from .debugger import DebuggerInterface

T = TypeVar("T")


class PyDebugger(DebuggerInterface):
    """
    Python language support of the DebuggerInterface.
    """

    def __init__(self, callbacks: ControllerCallbacksInterface) -> None:
        print("PyDebugger created")
        pass

    def set_code(self, code: str) -> None:
        pass

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        pass

    def backward_step(self) -> None:
        pass

    def forward_step(self) -> None:
        pass

    def forward_step_into(self) -> None:
        pass

    def step_into(self) -> None:
        pass

    def do_continue(self) -> None:
        pass
