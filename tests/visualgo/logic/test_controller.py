""":demand: F1.8"""

import unittest
from visualgo.logic import Controller, DebuggerInterface, ControllerCallbacksInterface, UICallbacksInterface, TransferVariables, Statistics
from visualgo.logic.controller import ExecutionState

import trio.testing
import asyncio

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
    def __init__(self,):
        pass

    def initialize(self, callbacks: ControllerCallbacksInterface) -> None:
        self.__controller_callbacks = callbacks
        pass

    def set_code(self, code: str) -> None:
        pass

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        pass

    def del_breakpoint(self, line_number: int) -> None:
        pass

    def next(self) -> None:
        self.__controller_callbacks.next_done(None, 0)
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
        controller = Controller(MockPyDebugger, MockUICallbacks())
        self.assertIsInstance(controller, Controller)

    def test_set_step_time(self):
        controller = Controller(MockPyDebugger, MockUICallbacks())
        controller.set_step_time(0.5)
        self.assertEqual(controller._Controller__step_time, 0.5)

    def test_pause_continue(self):
        async def trio_test_pause_continue():
            # controller = Controller(MockPyDebugger, MockUICallbacks())
            # controller._Controller__execution_state = ExecutionState.STOPPED
            # controller.set_step_time(0.5)
            # await controller.pause_continue()
            # self.assertEqual(controller._Controller__execution_state, ExecutionState.RUNNING)
            # await asyncio.sleep(1) # Wait for at least 1 call to forward_step()
            # controller._Controller__execution_state = ExecutionState.STOPPED

            controller = Controller(MockPyDebugger, MockUICallbacks())
            controller._Controller__execution_state = ExecutionState.RUNNING
            await controller.pause_continue()
            self.assertEqual(controller._Controller__execution_state, ExecutionState.STOPPED)

        asyncio.run(trio_test_pause_continue())

    # def test_start(self):
    #     async def trio_test_start():
    #         controller = Controller(MockPyDebugger, MockUICallbacks())
    #         await controller.start()
    #         controller.set_step_time(0.5)
    #         await asyncio.sleep(1) # Wait for at least 1 call to forward_step()
    #         controller.pause_continue()
    #         pass

    #     asyncio.run(trio_test_start)



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# if __name__ == '__main__':
#     unittest.main()
