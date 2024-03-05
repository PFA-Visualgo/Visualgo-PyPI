from .controller import Controller
from .ui.ui_callbacks import UICallbacksInterface
from .ui.ui_callbacks import TransferVariables
from .types import Statistics
from .debugger.py_debugger import PyDebugger

class UICallbacks(UICallbacksInterface):
    def update_variables(self, vars: TransferVariables) -> None:
        pass

    def update_statistics(self, stats: Statistics) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass

    def get_code(self) -> str:
        pass

controller = Controller(PyDebugger(), UICallbacks()) # haven't tested this yet

print("Hello, World!")
