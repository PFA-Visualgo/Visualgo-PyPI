from .controller import Controller
from .ui.ui_callbacks import UICallbacksInterface
from .ui.ui_callbacks import TransferVars
from .stats import Stats


class UICallbacks(UICallbacksInterface):
    def update_variables(self, vars: TransferVars) -> None:
        pass

    def update_statistics(self, stats: Stats) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass


callbacks = UICallbacks()
controller = Controller(callbacks)


print("Hello, World!")
