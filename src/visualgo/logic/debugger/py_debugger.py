from typing import TypeVar
import sys

from ..controller_callbacks import ControllerCallbacksInterface
from __private.comm_api import to_worker
from .debugger import AbstractDebugger

T = TypeVar("T")


class PyAbstractDebugger(AbstractDebugger):
    """
    Python language support of the DebuggerInterface.
    """

    def __init__(self, callbacks: ControllerCallbacksInterface) -> None:
        super().__init__(callbacks)
        to_worker.get_implementation().set_message_handler(self.dispatch_calls)

    def dispatch_calls(self, mes_id: str, mes_data):
        if mes_id == "EXEC_PAUSED":
            self.callbacks.execution_paused(mes_data[0], mes_data[1])
        elif mes_id == "EXEC_DONE":
            self.callbacks.execution_done(mes_data[0], mes_data[1])
        elif mes_id == "EXEC_THROWED":
            self.callbacks.on_error(mes_data[0])
        else:
            print(f"Unexpected message: {mes_id}", file=sys.stderr)

    def stop(self) -> None:
        print("worker interrupted", file=sys.stderr)
        to_worker.get_implementation().interrupt_worker()  # TODO: A voir

    def set_code(self, code: str) -> None:
        to_worker.get_implementation().send_message("SET_CODE", (code,))

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        to_worker.get_implementation().send_message("ADD_BP", (line_number, cond))

    def del_breakpoint(self, line_number: int) -> None:
        to_worker.get_implementation().send_message("DEL_BP", (line_number,))

    def backward_step(self) -> None:
        to_worker.get_implementation().send_message("BW_S", None)

    def forward_step(self) -> None:
        to_worker.get_implementation().send_message("FW_S", None)

    def forward_next(self) -> None:
        to_worker.get_implementation().send_message("FW_N", None)

    def do_continue(self) -> None:
        to_worker.get_implementation().send_message("CONT", None)
