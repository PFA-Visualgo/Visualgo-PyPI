""":demand: F1.8"""

import unittest
from visualgo.logic import Controller, DebuggerInterface, ControllerCallbacksInterface, UICallbacksInterface, TransferVariables, Statistics

class MockUICallbacks(UICallbacksInterface):
    def set_current_line(self, line: int) -> None:
        pass

    def update_variables(self, vars: TransferVariables) -> None:
        pass

    def update_statistics(self, stats: Statistics) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass

    def get_code(self) -> str:
        return "Hello, World!"

    def show_message(self, message: str) -> None:
        print(message)
        pass


class MockPyDebugger(DebuggerInterface):
    def __init__(self, controller_callbacks: ControllerCallbacksInterface):
        self.__controller_callbacks = controller_callbacks
        pass

    def set_code(self, code: str) -> None:
        pass

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        pass

    def step_into(self) -> None:
        self.__controller_callbacks.step_into_done(None, 0)
        pass

    def forward_step(self) -> None:
        self.__controller_callbacks.forward_step_done(None, 0)
        pass

    def backward_step(self) -> None:
        self.__controller_callbacks.backward_step_done(None, 0)
        pass

    def do_continue(self) -> None:
        self.__controller_callbacks.do_continue_done(None, 0)
        pass




class TestController(unittest.TestCase):
    def test_creation(self):
        print("Testing Controller creation")
        controller = Controller(MockPyDebugger, MockUICallbacks())
        self.assertIsInstance(controller, Controller)
        controller.start()
        print("Controller created successfully")


if __name__ == '__main__':
    unittest.main()
