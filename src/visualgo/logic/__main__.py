from .controller import Controller
from .ui.ui_callbacks import UICallbacksInterface
from .ui.ui_callbacks import TransferVariables
from .types import Statistics


class UICallbacks(UICallbacksInterface):
    def update_variables(self, vars: TransferVariables) -> None:
        pass

    def update_statistics(self, stats: Statistics) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass

    def get_code(self) -> str:
        pass

# Debugger as parameter
# controller = Controller(PyDebugger("print('Hello World!')"), UICallbacks())


# Debugger from package
controller = Controller(UICallbacks())

controller.start("print('Hello, World!')")
