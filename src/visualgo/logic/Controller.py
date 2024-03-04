import typing
from . import Variables, Statistics, TransferVariables, TransferStatistics, CodeError, \
            SymboleDescription, StaticVariables, UICallbacksInterface, ExecutionState

class Controller:
    def __init__(self, ui_interface : UICallbacksInterface) -> None:
        """
        Initializes the Controller with the given `ui_interface`.
        :param ui_interface: UICallbacksInterface
        :return: None
        """

        self.__ui_interface = ui_interface
        self.__execution_state = ExecutionState.NOT_INITIALIZED
        self.__current_statistics : Statistics = None
        self.__current_variables : Variables = None
        self.__code : str = None
        self.__step_time : int = 500
        pass

    def __initialize_debugger(self, code: str) -> None:
        """
        Initializes the debugger with the given `code`.
        :param code: str
        :return: None
        """
        self.__code = code
        self.__execution_state = ExecutionState.RUNNING
        pass

    def __end_of_execution(self) -> None:
        """
        Ends the execution of the code.
        :return: None
        """
        self.__execution_state = ExecutionState.FINISHED
        pass

    def __get_ui_stats(self, stats: Statistics, tracked_funs : typing.List[SymboleDescription]) -> \
            Statistics:
        """
        Returns the statistics of the execution given the debugger `stats` and the user parameters
        `tracked_funs`.
        :param stats: Statistics
        :param variables: typing.List[TransferVariable]
        :return: Statistics
        """
        pass

    def __get_ui_vars(self, variables: Variables, tracked_vars : typing.List[SymboleDescription]) -> \
            Variables:
        """
        Returns the variables of the execution given the debugger `variables` and the user parameters
        `tracked_vars`.
        :param variables: Variables
        :param variables: typing.List[TransferVariable]
        :return: Variables
        """
        pass

    def start(self) -> None:
        """
        Starts the execution of the code.
        :return: None
        """
        self.__initialize_debugger(self.__ui_interface.get_code())
        pass

    def pause_continue(self) -> None:
        """
        Pauses or continues the execution of the code.
        :return: None
        """
        if self.__execution_state == ExecutionState.RUNNING:
            self.__execution_state = ExecutionState.STOPPED
        else:
            self.__execution_state = ExecutionState.RUNNING
        pass

    def set_step_time(self, time: int) -> None:
        """
        Sets the time of the step to `time` in milliseconds.

        :param time: int
            The time to set for the step.
        :raises ValueError:
            If the specified time is less than or equal to 0.
        :return: None
        """
        try:
            if time <= 0:
                raise ValueError("Time must be greater than 0")
            self.__step_time = time
        except ValueError as e:
            print(f"Error: {e}")
        pass

    def forward_step(self) -> None:
        """
        Executes the next line of the code.
        :return: None
        """
        pass

    def forward_next(self) -> None:
        """
        Executes the next line of the code without entering into the user function.
        :return: None
        """
        pass

    def backward_step(self) -> None:
        """
        Executes the previous line of the code.
        :return: None
        """
        raise NotImplementedError("Method not yet implemented")
        pass

    def backward_next(self) -> None:
        """
        Executes the previous line of the code without entering into the user function.
        :return: None
        """
        raise NotImplementedError("Method not yet implemented")
        pass

    def get_csv(self) -> str:
        """
        Returns the evolution of the statistics at the checkpoints/breakpoints in a CSV format.
        :return: str
        """
        pass

    def get_static_variables(self) -> StaticVariables:
        """
        Returns the variables defined in the code before the execution.
        :return: Variables
        """
        pass

    def new_checkpoint(self, line_number: int) -> None:
        """
        Add a new checkpoint at the given `line_number`.
        :param line_number: int
        :return: None
        """
        pass

    def new_breakpoint(self, line_number: int) -> None:
        """
        Add a new breakpoint at the given `line_number`.
        :param line_number: int
        :return: None
        """
        pass

    def new_tracked_variable(self, variable: SymboleDescription) -> None:
        """
        Add a new tracked variable by the user with the given `variable`.
        :param variable: SymboleDescription
        :return: None
        """
        pass

    def new_tracked_function(self, function: SymboleDescription) -> None:
        """
        Add a new tracked function by the user with the given `function`.
        :param function: SymboleDescription
        :return: None
        """
        pass

    def del_checkpoint(self, line_number: int) -> None:
        """
        Delete the checkpoint at the given `line_number`.
        :param line_number: int
        :return: None
        """
        pass

    def del_breakpoint(self, line_number: int) -> None:
        """
        Delete the breakpoint at the given `line_number`.
        :param line_number: int
        :return: None
        """
        pass

    def del_tracked_variable(self, variable: SymboleDescription) -> None:
        """
        Delete the tracked variable with the given `variable`.
        :param variable: SymboleDescription
        :return: None
        """
        pass

    def del_tracked_function(self, function: SymboleDescription) -> None:
        """
        Delete the tracked function with the given `function`.
        :param function: SymboleDescription
        :return: None
        """
        pass


