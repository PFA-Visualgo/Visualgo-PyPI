from enum import Enum

from .debugger.debugger_callbacks import DebuggerCallbacksInterface
from .debugger.py_debugger import PyDebugger
from .debugger.debug_types import DebugVars
from .stats import Stats
from .static.static_analysis import StaticVars
from .ui.ui_callbacks import UICallbacksInterface


class SymbolDesc:
    pass


class StatsAtCheckpoints:
    pass


class ExecutionState(Enum):
    NOT_INITIALIZED = 0
    RUNNING = 1
    STOPPED = 2
    FINISHED = 3


class Controller:

    def __init__(self, ui_callbacks: UICallbacksInterface) -> None:
        self.execution_state: ExecutionState = ExecutionState.NOT_INITIALIZED
        self.current_stats: Stats = None
        self.current_vars: DebugVars = None
        self.ui_callbacks: UICallbacksInterface = ui_callbacks
        debugger_callbacks: DebuggerCallbacksInterface = self.__initialize_debugger_callbacks()
        self.debugger: PyDebugger = PyDebugger("", debugger_callbacks)

    # Private methods
    def __initialize_debugger(self, code: str, line_start: int) -> None:
        pass

    def __end_of_execution(self) -> None:
        pass

    def __ui_stats(
        self,
        stats: Stats,
        tracked_types: list[SymbolDesc],
        tracked_vars: list[SymbolDesc],
        tracked_functions: list[SymbolDesc],
    ) -> Stats:
        pass

    def __ui_vars(
            self, vars: DebugVars, tracked_vars: list[SymbolDesc]) -> DebugVars:
        pass

    def __initialize_debugger_callbacks(self) -> DebuggerCallbacksInterface:
        pass

    class DebuggerCallbacks(DebuggerCallbacksInterface):
        def __init__(self, controller: "Controller") -> None:
            self.controller: Controller = controller

    # Checkpoints
    def new_checkpoint(self, line_number: int) -> None:
        pass

    def del_checkpoint(self, line_number: int) -> None:
        pass

    # Breakpoints
    def new_breakpoint(self, line_number: int) -> None:
        pass

    def del_breakpoint(self, line_number: int) -> None:
        pass

    # Tracking
    def new_tracked_type(self, type_name: str, depth: int) -> None:
        pass

    def del_tracked_type(self, type_name: str, depth: int) -> None:
        pass

    def new_tracked_variable(self, var_name: str, depth: int) -> None:
        pass

    def del_tracked_variable(self, var_name: str, depth: int) -> None:
        pass

    def new_tracked_function(self, function_name: str, depth: int) -> None:
        pass

    def del_tracked_function(self, function_name: str, depth: int) -> None:
        pass

    # Debugger
    def start(self, code: str) -> None:
        pass

    def pause_continue(self) -> None:
        pass

    def set_automatic_step_time(self, value: int) -> None:
        pass

    def forward_next(self) -> None:
        pass

    def forward_step(self) -> None:
        pass

    def backward_next(self) -> None:
        pass

    def backward_step(self) -> None:
        pass

    # Statistics
    def get_csv(self) -> StatsAtCheckpoints:
        pass

    def get_static_variables(self, code: str) -> StaticVars:
        pass
