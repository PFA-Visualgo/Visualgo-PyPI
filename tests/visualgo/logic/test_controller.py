""":demand: F1.8"""

import unittest
from visualgo.logic import Controller, DebuggerInterface, ControllerCallbacksInterface, UICallbacksInterface, TransferVariables, Statistics 
from visualgo.logic.debugger.types import DebugContext
from visualgo.logic.controller import ExecutionState

import asyncio

mock_py_debugger_logs = []  # List to store logs of calls from the Controller to the MockPyDebugger

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
    
    def __init__(self):
        self.vars = DebugContext("filepath", 0, None)
        global mock_py_debugger_logs
        mock_py_debugger_logs = [] 

    def initialize(self, callbacks: ControllerCallbacksInterface) -> None:
        self.__controller_callbacks = callbacks
        mock_py_debugger_logs.append("initialize")

    def set_code(self, code: str) -> None:
        mock_py_debugger_logs.append("set_code")

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        mock_py_debugger_logs.append(f"add_breakpoint {line_number} {cond}")

    def del_breakpoint(self, line_number: int) -> None:
        mock_py_debugger_logs.append(f"del_breakpoint {line_number}")

    async def step_into(self) -> None:
        mock_py_debugger_logs.append("step_into")
        await self.__controller_callbacks.execution_paused(self.vars, 0)

    async def forward_step(self) -> None:
        mock_py_debugger_logs.append("forward_step")
        await self.__controller_callbacks.execution_paused(self.vars, 0)

    async def backward_step(self) -> None:
        mock_py_debugger_logs.append("backward_step")
        await self.__controller_callbacks.execution_paused(self.vars, 0)

    async def do_continue(self) -> None:
        mock_py_debugger_logs.append("do_continue")
        await self.__controller_callbacks.execution_paused(self.vars, 0)
    
    def stop(self) -> None:
        mock_py_debugger_logs.append("stop")
        self.__controller_callbacks.execution_done(self.vars, 0)


step_time = 0.001 # stupidly low value to speed up tests

class TestController(unittest.TestCase):


    def test_creation(self):
        controller = Controller(MockPyDebugger, MockUICallbacks())
        self.assertIsInstance(controller, Controller)
        assert controller._Controller__debugger is not None
        assert mock_py_debugger_logs[0] == "initialize"

    def test_set_step_time(self):
        controller = Controller(MockPyDebugger, MockUICallbacks())
        controller.set_step_time(0.5)
        self.assertEqual(controller._Controller__step_time, 0.5)

    def test_pause_continue(self):
        async def async_test_pause_continue():
            # Test case 1 : Pause the controller
            controller = Controller(MockPyDebugger, MockUICallbacks())
            controller._Controller__execution_state = ExecutionState.RUNNING
            await controller.pause_continue()
            self.assertEqual(controller._Controller__execution_state, ExecutionState.PAUSED)

            # Test case 2 : Unpause the controller
            controller = Controller(MockPyDebugger, MockUICallbacks(), 5)
            controller._Controller__execution_state = ExecutionState.PAUSED
            controller.set_step_time(step_time) 
            await controller.pause_continue()
            # The controller should be running for 5 steps then pause
            assert len(mock_py_debugger_logs) == 6
            assert mock_py_debugger_logs[0] == "initialize"
            assert mock_py_debugger_logs[1] == "forward_step"
            assert mock_py_debugger_logs[2] == "forward_step"
            assert mock_py_debugger_logs[3] == "forward_step"
            assert mock_py_debugger_logs[4] == "forward_step"
            assert mock_py_debugger_logs[5] == "forward_step"
            assert controller.recursion_depth == 5
            assert controller._Controller__execution_state == ExecutionState.PAUSED

        asyncio.run(async_test_pause_continue())

    def test_start(self):
        async def async_test_start():
            # Test case 1 : Start the controller
            controller = Controller(MockPyDebugger, MockUICallbacks(), 5)
            controller.set_step_time(step_time)
            await controller.start()
            # The controller should be running for 5 steps then pause
            assert len(mock_py_debugger_logs) == 7
            assert mock_py_debugger_logs[0] == "initialize"
            assert mock_py_debugger_logs[1] == "set_code"
            assert mock_py_debugger_logs[2] == "forward_step"
            assert mock_py_debugger_logs[3] == "forward_step"
            assert mock_py_debugger_logs[4] == "forward_step"
            assert mock_py_debugger_logs[5] == "forward_step"
            assert mock_py_debugger_logs[6] == "forward_step"
            assert controller.recursion_depth == 5
            assert controller._Controller__execution_state == ExecutionState.PAUSED

        asyncio.run(async_test_start())



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# if __name__ == '__main__':
#     unittest.main()