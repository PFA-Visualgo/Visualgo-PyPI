from . import DebugContext

class DebuggerCallbacksInterface:
    def __init__(self):
        pass

    def backward_step_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        raise NotImplementedError("Method not implemented")
        pass

    def forward_step_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        raise NotImplementedError("Method not implemented")
        pass

    def forward_step_into_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        raise NotImplementedError("Method not implemented")
        pass

    def backward_step_into_done(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        raise NotImplementedError("Method not implemented")
        pass

    def breakpoint_reached(self, context : DebugContext, line_number : int) -> None:
        """
        Return the debug context and the line number where the execution stopped to the Controller.
        :param context: DebugContext
        :param line_number: int
        :return: None
        """
        raise NotImplementedError("Method not implemented")
        pass
