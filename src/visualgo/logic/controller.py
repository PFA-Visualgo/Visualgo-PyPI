from enum import Enum
from abc import ABC, abstractmethod
import asyncio


from .types import Statistics, SymbolDescription, CodeError
from .controller_callbacks import ControllerCallbacksInterface

from .debugger.types import DebugContext, DebugVariables
from .debugger.debugger import DebuggerInterface
from .debugger.py_debugger import PyDebugger

from .static.types import StaticVariables

from .ui.types import TransferVariable, TransferVariables
from .ui.ui_callbacks import UICallbacksInterface


class ExecutionState(Enum):
    """
    Enum for the different states of the execution for the Controller.

    :demand: F.2.4
    """
    NOT_INITIALIZED = 0
    RUNNING = 1
    PAUSED = 2
    FINISHED = 3


class ControllerInterface(ABC):
    """
    Interface for the Controller class.
    """

    # Execution control
    @abstractmethod
    def start(self) -> None:
        """
        Starts the execution of the code.

        :demand: F.1.6
        :return: None
        """
        pass

    @abstractmethod
    def stop(self) -> None:
        """
        Stops the execution of the code. Basically resets the debugger

        :demand: ?
        :return:
        """
        pass

    @abstractmethod
    def pause_continue(self) -> None:
        """
        Pauses or continues the execution of the code.

        :demand: F.2.4
        :return: None
        """
        pass

    @abstractmethod
    def set_step_time(self, time: int) -> None:
        """
        Sets the time of the step to `time` in milliseconds.

        :param time: int
            The time to set for the step.
        :raises ValueError:
            If the specified time is less than or equal to 0.
        :return: None
        """
        pass

    @abstractmethod
    def forward_step(self) -> None:
        """
        Executes the next line of the code.

        :return: None
        """
        pass

    @abstractmethod
    def forward_next(self) -> None:
        """
        Executes the next line of the code without entering into the user function.

        :return: None
        """
        pass

    @abstractmethod
    def backward_step(self) -> None:
        """
        Executes the previous line of the code.

        :return: None
        """
        pass

    # Checkpoints
    @abstractmethod
    def new_checkpoint(self, line_number: int) -> None:
        """
        Add a new checkpoint at the given `line_number`.

        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def del_checkpoint(self, line_number: int) -> None:
        """
        Delete the checkpoint at the given `line_number`.

        :param line_number: int
        :return: None
        """
        pass

    # Breakpoints
    @abstractmethod
    def new_breakpoint(self, line_number: int) -> None:
        """
        Add a new breakpoint at the given `line_number`.

        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def del_breakpoint(self, line_number: int) -> None:
        """
        Delete the breakpoint at the given `line_number`.

        :param line_number: int
        :return: None
        """
        pass

    # Tracking for drawings
    @abstractmethod
    def new_tracked_variable(self, variable: SymbolDescription) -> None:
        """
        Add a new tracked variable by the user with the given `variable`.

        :demand: F.2.7
        :param variable: SymbolDescription
        :return: None
        """
        pass

    @abstractmethod
    def del_tracked_variable(self, variable: SymbolDescription) -> None:
        """
        Delete the tracked variable with the given `variable`.

        :demand: F.2.7
        :param variable: SymbolDescription
        :return: None
        """
        pass

    # Tracking for statistics
    @abstractmethod
    def new_tracked_function(self, function: SymbolDescription) -> None:
        """
        Add a new tracked function by the user with the given `function`.

        :demand: F.2.8
        :param function: SymbolDescription
        :return: None
        """
        pass

    @abstractmethod
    def del_tracked_function(self, function: SymbolDescription) -> None:
        """
        Delete the tracked function with the given `function`.

        :demand: F.2.8
        :param function: SymbolDescription
        :return: None
        """
        pass

    @abstractmethod
    def new_tracked_type(self, type_name: str) -> None:
        """
        Add a new tracked type by the user with the given `type_name`.

        :demand: F.2.8
        :param type_name: str
        :return: None
        """
        pass

    @abstractmethod
    def del_tracked_type(self, type_name: str) -> None:
        """
        Delete the tracked type with the given `type_name`.

        :demand: F.2.8
        :param type_name: str
        :return: None
        """
        pass

    # Statistics
    @abstractmethod
    def get_csv(self) -> str:
        """
        Returns the evolution of the statistics at the checkpoints/breakpoints in a CSV format.
        Format of the CSV to be determined...

        :return: str
        """
        pass

    @abstractmethod
    def get_static_variables(self) -> StaticVariables:
        """
        Returns the variables defined in the code before the execution.

        :demand: F.2.7
        :return: Variables
        """
        pass


class Controller(ControllerCallbacksInterface, ControllerInterface):
    """
    Controller class that manages the interaction between the UI and the Debugger.
    Implements the ControllerCallbacksInterface to receive notifications from
    the Debugger, and the ControllerInterface to receive calls from the UI.
    """

    def __init__(self, debugger_class: type,
                 ui_callbacks: UICallbacksInterface,
                 max_recursion_depth: int = None) -> None:
        """
        Initializes the Controller with the given a `debugger_class` that will be instantiated and
        a `ui_callbacks` to communicate with the UI. 
        Also can use the `max_recursion_depth` for testing purposes.

        :demand: F.1.5
        :demand: F.2.7
        :demand: F.2.8
        :param debugger_class: type
        :param ui_callbacks: UICallbacksInterface
        :return: None
        """
        # private attributes
        self.__ui_callbacks: UICallbacksInterface = ui_callbacks
        self.__execution_state: ExecutionState = ExecutionState.NOT_INITIALIZED

        # self.__current_statistics: Statistics = None
        # self.__current_variables: DebugVariables = None
        self.__tracked_vars: list[SymbolDescription] = []
        self.__tracked_funs: list[SymbolDescription] = []
        self.__tracked_types: list[str] = []

        self.__checkpoints: list[int] = []
        self.__breakpoints: list[int] = []

        self.__step_time: int = 500
        self.__debugger: DebuggerInterface = debugger_class()
        self.__debugger.initialize(self)

        self.__recursion_depth: int = 0
        self.__max_recursion_depth: int = max_recursion_depth

    # Private methods
    def __initialize_debugger(self, code: str) -> None:
        """
        Initializes the debugger with the given `code`.

        :param code: str
        :return: None
        """
        self.__debugger.set_code(code)
        self.__execution_state = ExecutionState.RUNNING

    def __end_of_execution(self) -> None:
        """
        Ends the execution of the code.

        :return: None
        """
        self.__execution_state = ExecutionState.FINISHED

    def __get_ui_stats(self, stats: Statistics,
                       tracked_types: list[SymbolDescription],
                       tracked_funs: list[SymbolDescription]) -> Statistics:
        """
        Returns the statistics of the execution given the debugger `stats`
        and the user parameters `tracked_types` and `tracked_funs`.
        TODO: Remove tracked_types and tracked_funs ? Accessible from self.

        :demand: F.1.5
        :param stats: Statistics
        :param tracked_types: list[SymbolDescription]
        :param tracked_funs: list[SymbolDescription]
        :return: Statistics
        """
        pass

    def __get_transfer_vars(
            self, vars: DebugVariables, function_name: str, depth: int) -> TransferVariables:
        """
        Returns the variables of the execution given the `frame`.

        :param vars: DebugVariables
        :param function_name: str
        :param depth: int
        :return: TransferVariables
        """
        res = []
        for name, value in vars.locals.items():
            desc = SymbolDescription(name, function_name, depth)
            ui_var = TransferVariable(desc, value)
            res.append(ui_var)
        return TransferVariables(res)

    def __get_ui_vars(
            self, context: DebugContext,
            tracked_vars: list[SymbolDescription]) -> TransferVariables:
        """
        Returns the variables of the execution given the debugger
        `variables` and the user parameters `tracked_vars`.
        TODO: Remove tracked_vars ? Accessible from self.

        :param context: DebugContext
        :param tracked_vars: typing.List[SymbolDescription]
        :return: TransferVariables
        """
        res = []
        depth = 0
        for debug_vars in context.variables[::-1]:
            # TODO: Once merged, function_name will probably be in DebugVariables
            # (and thus accessible from debug_vars)
            function_name = debug_vars.function_name
            res += self.__get_transfer_vars(debug_vars, function_name, depth)
            depth += 1

        if len(tracked_vars) == 0:
            return TransferVariables(res)

        allowed = [var.name for var in tracked_vars]

        for var in res:
            if var.description.name not in allowed:
                res.remove(var)

    def __update_ui(self, context: DebugContext) -> None:
        """
        Updates the UI with the given `context`.

        :param context: DebugContext
        :return: None
        """
        vars = self.__get_ui_vars(context, self.__tracked_vars)
        self.__ui_callbacks.update_variables(vars)

    # ControllerCallbacksInterface

    async def execution_paused(self, context: DebugContext, line_number: int) -> None:
        """
        Update the visualisation once the debugger has finished executing code
        and is awaiting further instructions.
        Occurs on steps, next and continues.
        TODO: Update statistics here.
        TODO: Using "continue", we only update the UI when we reach a checkpoint / stop
        (here the ui is updated every time, as we consider only automatic mode for now)

        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        self.__ui_callbacks.set_current_line(line_number)

        if line_number in self.__checkpoints:  # Update UI and continue
            self.__update_ui(context)

            await asyncio.sleep(self.__step_time / 1000)
            self._add_recursion_depth()
            self.forward_step()
            return

        if line_number in self.__breakpoints:  # Update UI and pause
            self.__update_ui(context)
            self.__execution_state = ExecutionState.PAUSED
            return

        # Assume we are in automatic mode
        self.__update_ui(context)  # In automatic mode, we update the UI
        await asyncio.sleep(self.__step_time / 1000)
        self._add_recursion_depth()
        await self.forward_step()

    def execution_done(self, context: DebugContext, line_number: int) -> None:
        self.__update_ui(context)
        self.__ui_callbacks.set_current_line(line_number)  # Could be 0 too
        self.__end_of_execution()

    def on_error(self, error: CodeError) -> None:
        self.__ui_callbacks.show_error(error)

    def on_message(self, message: str) -> None:
        self.__ui_callbacks.show_message(message)

    # ControllerInterface
    def __pause_if_max_recursion_reached(self) -> None:
        if self.__max_recursion_depth is not None:
            if self.__recursion_depth >= self.__max_recursion_depth:
                self.__execution_state = ExecutionState.PAUSED

    @property
    def recursion_depth(self) -> int:
        return self.__recursion_depth

    def _add_recursion_depth(self) -> None:
        self.__recursion_depth += 1
        self.__pause_if_max_recursion_reached()

    def __check_if_initialized(self) -> None:
        if self.__execution_state == ExecutionState.NOT_INITIALIZED:
            self.__ui_callbacks.show_error("Controller not initialized")
            raise ValueError("Controller not initialized")

    async def start(self) -> None:
        print("in start")
        code = self.__ui_callbacks.get_code()
        self.__initialize_debugger(code)
        self.__execution_state = ExecutionState.RUNNING
        self.__recursion_depth = 0
        print("before loop_forward_step")
        await self.forward_step()
        print("after loop_forward_step")

    async def pause_continue(self) -> None:
        self.__recursion_depth = 0
        if self.__execution_state == ExecutionState.RUNNING:
            self.__execution_state = ExecutionState.PAUSED
        else:
            self.__execution_state = ExecutionState.RUNNING
            await self.forward_step()

    def stop(self) -> None:
        """
        Stops the execution of the code. Basically resets the debugger

        :demand: ?
        :return:
        """
        self.__debugger.stop()
        self.__execution_state = ExecutionState.NOT_INITIALIZED

    def set_step_time(self, time: int) -> None:
        if time <= 0:
            self.__ui_callbacks.show_error("Time must be greater than 0")
        else:
            self.__step_time = time

    async def forward_step(self) -> None:
        # TODO: forward_step and forward_next are the same
        # One should call debugger.step_into, the other forward_step ?
        self.__check_if_initialized()
        if self.__execution_state == ExecutionState.RUNNING:
            await self.__debugger.forward_step()

    async def forward_next(self) -> None:
        self.__check_if_initialized()
        if self.__execution_state == ExecutionState.RUNNING:
            await self.__debugger.forward_step()

    def backward_step(self) -> None:
        self.__check_if_initialized()
        if self.__execution_state == ExecutionState.RUNNING:
            self.__debugger.backward_step()

    # Checkpoints
    def new_checkpoint(self, line_number: int, cond: str) -> None:
        # maybe TODO change how the condition is passed
        self.__debugger.add_breakpoint(line_number, "")
        self.__checkpoints.append(line_number)

    def del_checkpoint(self, line_number: int) -> None:
        self.__debugger.del_breakpoint(line_number)
        self.__checkpoints.remove(line_number)

    # Breakpoints
    def new_breakpoint(self, line_number: int, cond: str) -> None:
        # maybe TODO change how the condition is passed
        self.__debugger.add_breakpoint(line_number, "")
        self.__breakpoints.append(line_number)

    def del_breakpoint(self, line_number: int) -> None:
        self.__debugger.del_breakpoint(line_number)
        self.__breakpoints.remove(line_number)

    # Tracking for drawings
    def new_tracked_variable(self, variable: SymbolDescription) -> None:
        self.__tracked_vars.append(variable)

    def del_tracked_variable(self, variable: SymbolDescription) -> None:
        self.__tracked_vars.remove(variable)

    # Tracking for statistics
    def new_tracked_function(self, function: SymbolDescription) -> None:
        self.__tracked_funs.append(function)

    def del_tracked_function(self, function: SymbolDescription) -> None:
        self.__tracked_funs.remove(function)

    def new_tracked_type(self, type_name: str) -> None:
        self.__tracked_types.append(type_name)

    def del_tracked_type(self, type_name: str) -> None:
        self.__tracked_types.remove(type_name)

    # Statistics
    def get_csv(self) -> str:
        raise NotImplementedError("Method not yet implemented")

    def get_static_variables(self) -> StaticVariables:
        raise NotImplementedError("Method not yet implemented")
