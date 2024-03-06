""":demand: F1.8"""

import unittest
from visualgo.logic import Controller, UICallbacksInterface, TransferVariables, Statistics, PyDebugger
from visualgo.logic import Controller

class UICallbacks(UICallbacksInterface):
    def update_variables(self, vars: TransferVariables) -> None:
        pass

    def update_statistics(self, stats: Statistics) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass

    def get_code(self) -> str:
        pass

class TestController(unittest.TestCase):
    def test_creation(self):
        print("Testing Controller creation")
        controller = Controller(PyDebugger, UICallbacks())
        self.assertIsInstance(controller, Controller)
        controller.start("print('Hello, World!')")
        print("Controller created successfully")


if __name__ == '__main__':
    unittest.main()
