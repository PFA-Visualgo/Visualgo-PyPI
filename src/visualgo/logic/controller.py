from enum import Enum
from abc import ABC, abstractmethod

from .types import Statistics, SymbolDescription, CodeError
from .controller_callbacks import ControllerCallbacksInterface

from .debugger.types import DebugVariables, DebugContext
from .debugger.debugger import DebuggerInterface
from .debugger.py_debugger import PyDebugger

from .static.types import StaticVariables

from .ui.types import TransferVariables
from .ui.ui_callbacks import UICallbacksInterface


class ExecutionState(Enum):
    """
    Enum for the different states of the execution for the Controller.

    :demand: F.2.4
    """
    NOT_INITIALIZED = 0
    RUNNING = 1
    STOPPED = 2
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

    @abstractmethod
    def backward_next(self) -> None:
        """
        Executes the previous line of the code without entering into the user function.

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
        :param variable: SymboleDescription
        :return: None
        """
        pass

    @abstractmethod
    def del_tracked_variable(self, variable: SymbolDescription) -> None:
        """
        Delete the tracked variable with the given `variable`.

        :demand: F.2.7
        :param variable: SymboleDescription
        :return: None
        """
        pass

    # Tracking for statistics
    @abstractmethod
    def new_tracked_function(self, function: SymbolDescription) -> None:
        """
        Add a new tracked function by the user with the given `function`.
        
        :demand: F.2.8
        :param function: SymboleDescription
        :return: None
        """
        pass

    @abstractmethod
    def del_tracked_function(self, function: SymbolDescription) -> None:
        """
        Delete the tracked function with the given `function`.

        :demand: F.2.8
        :param function: SymboleDescription
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

    def __init__(self, debugger_class: type, ui_callbacks: UICallbacksInterface):
        """
        Initializes the Controller with the given a `debugger_class` that will be instantiated and
        a `ui_callbacks` to communicate with the UI.

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
        self.__current_statistics: Statistics = None
        self.__current_variables: DebugVariables = None
        self.__step_time: int = 500
        self.__debugger: DebuggerInterface = debugger_class(self)

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

        :demand: F.1.5
        :param stats: Statistics
        :param variables: typing.List[SymboleDescription]
        :return: Statistics
        """
        pass

    def __ui_vars(
            self, vars: DebugVariables,
            tracked_vars: list[SymbolDescription]) -> DebugVariables:
        """
        Returns the variables of the execution given the debugger
        `variables` and the user parameters `tracked_vars`.
        
        :param variables: Variables
        :param variables: typing.List[SymboleDescription]
        :return: Variables
        """
        pass

    ## ControllerCallbacksInterface
    def backward_step_done(self, context: DebugContext, line_number: int) -> None:
        # self.__ui_callbacks.update_variables(self.__ui_vars(context.variables, []))
        raise NotImplementedError("Method not yet implemented")

    def forward_step_done(self, context: DebugContext, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def step_into_done(self, context: DebugContext, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def backward_step_into_done(self, context: DebugContext, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def continue_done(self, context: DebugContext, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def end_of_code_reached(self, context: DebugContext, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def on_error(self, error: CodeError) -> None:
        raise NotImplementedError("Method not yet implemented")

    ## ControllerInterface
    def start(self) -> None:
        code = self.__ui_callbacks.get_code()
        self.__initialize_debugger(code)
        self.__ui_callbacks.update_variables(self.__current_variables) # Temporary for demonstration purposes

    def pause_continue(self) -> None:
        if self.__execution_state == ExecutionState.RUNNING:
            self.__execution_state = ExecutionState.STOPPED
        else:
            self.__execution_state = ExecutionState.RUNNING

    def set_step_time(self, time: int) -> None:
        try:
            if time <= 0:
                raise ValueError("Time must be greater than 0")
            self.__step_time = time
        except ValueError as e:
            print(f"Error: {e}")

    def forward_step(self) -> None:
        raise NotImplementedError("Method not yet implemented")

    def forward_next(self) -> None:
        raise NotImplementedError("Method not yet implemented")

    def backward_step(self) -> None:
        raise NotImplementedError("Method not yet implemented")

    def backward_next(self) -> None:
        raise NotImplementedError("Method not yet implemented")

    # Checkpoints
    def new_checkpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def del_checkpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    # Breakpoints
    def new_breakpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    def del_breakpoint(self, line_number: int) -> None:
        raise NotImplementedError("Method not yet implemented")

    # Tracking for drawings
    def new_tracked_variable(self, variable: SymbolDescription) -> None:
        raise NotImplementedError("Method not yet implemented")

    def del_tracked_variable(self, variable: SymbolDescription) -> None:
        raise NotImplementedError("Method not yet implemented")

    # Tracking for statistics
    def new_tracked_function(self, function: SymbolDescription) -> None:
        raise NotImplementedError("Method not yet implemented")

    def del_tracked_function(self, function: SymbolDescription) -> None:
        raise NotImplementedError("Method not yet implemented")

    def new_tracked_type(self, type_name: str) -> None:
        raise NotImplementedError("Method not yet implemented")

    def del_tracked_type(self, type_name: str) -> None:
        raise NotImplementedError("Method not yet implemented")

    # Statistics
    def get_csv(self) -> str:
        raise NotImplementedError("Method not yet implemented")

    def get_static_variables(self) -> StaticVariables:
        raise NotImplementedError("Method not yet implemented")
