from abc import ABC, abstractmethod

from .debugger.types import DebugContext

class ControllerCallbacksInterface(ABC):
    """
    Interface so that the debugger can call the controller when it has finished an action.
    """

    @abstractmethod
    def backward_step_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def forward_step_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def forward_step_into_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def backward_step_into_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def continue_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

    @abstractmethod
    def end_of_code_reached(self, vars: DebugContext, line_number: int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        pass

