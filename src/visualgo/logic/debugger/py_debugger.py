from typing import TypeVar

from ..controller_callbacks import ControllerCallbacksInterface
from .debugger import DebuggerInterface

T = TypeVar("T")


class PyDebugger(DebuggerInterface):
    """
    Python language support of the DebuggerInterface.
    """

    def __init__(self) -> None:
        print("PyDebugger created")

    def initialize(self, callbacks: ControllerCallbacksInterface) -> None:
        return

    def set_code(self, code: str) -> None:
        raise NotImplementedError("Method not implemented yet")

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        raise NotImplementedError("Method not implemented yet")

    def del_breakpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not implemented yet")

    def del_breakpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not implemented yet")

    def backward_step(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def forward_step(self) -> None:
        raise NotImplementedError("Method not implemented yet")
    
    def step_into(self) -> None:
        raise NotImplementedError("Method not implemented yet")

    def do_continue(self) -> None:
        raise NotImplementedError("Method not implemented yet")
    
    def stop(self) -> None:
        raise NotImplementedError("Method not implemented yet")
