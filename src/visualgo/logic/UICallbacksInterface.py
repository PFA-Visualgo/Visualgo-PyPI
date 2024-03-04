from . import TransferVariables, TransferStatistics, CodeError

class UICallbacksInterface:
    def update_variables(self, variables: TransferVariables) -> None:
        """
        Updates the variables in the UI with the given `variables`.
        :param variables: TransferVariables
        :return: None
        """
        raise NotImplementedError("Method not implemented")

    def update_statistics(self, statistics: TransferStatistics) -> None:
        """
        Updates the statistics in the UI with the given `statistics`.
        :param statistics: TransferStatistics
        :return: None
        """
        raise NotImplementedError("Method not implemented")

    def show_error(self, error: CodeError) -> None:
        """
        Shows the error in the UI with the given `error`.
        :param error: CodeError
        :return: None
        """
        raise NotImplementedError("Method not implemented")

    def get_code(self) -> str:
        """
        Returns the user code from the UI.
        :return: str
        """
        raise NotImplementedError("Method not implemented")


# Creates a subclass of UICallbacksInterface
# class UICallbacks(UICallbacksInterface):
#     ...
