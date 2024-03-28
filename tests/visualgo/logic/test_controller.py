""":demand: F1.8"""

import unittest
import types
import asyncio

from visualgo.logic import Controller, AbstractDebugger, ControllerCallbacksInterface, UICallbacksInterface, TransferVariables, Statistics 
from visualgo.logic.debugger import DebugContext, DebugVariables
from visualgo.logic.controller import ExecutionState
from visualgo.logic.ui import TransferVariable
from visualgo.logic import SymbolDescription


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

class MockDebugContext:
    @classmethod
    def list_from_frame(cls, frames: list[dict[str, dict[str, any]]]) -> list["MockDebugContext"]:
        """
        Creates a stack of DebugContext

        :param frame: The top-level frame
        :param botframe: The debugger's frame
        :return: A stack of DebugContext
        """
        lst = []
        n = len(frames)
        for i in range(n):
            lst.append(cls(frames[i], "filepath", 0, "function_name"))
        return lst

    def __init__(self, frame: dict[str, dict[str, any]], filepath: str, lineno: int, function_name: str):
        self.filepath = filepath
        self.lineno = lineno
        self.variables = None
        self.function_name = function_name
        if frame is None:
            return
        n = len(frame)
        self.variables = DebugVariables(frame["globals"], frame["locals"])

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
    
mock_py_debugger_logs = []  # List to store logs of calls from the Controller to the MockPyDebugger

class MockPyDebugger(AbstractDebugger):
    
    def __init__(self, callbacks: ControllerCallbacksInterface):
        self.__controller_callbacks = callbacks
        self.vars = MockDebugContext.list_from_frame([{ "globals": {"a": 1, "b": 2}, "locals": {"a": 1, "b": 2} }])
        global mock_py_debugger_logs
        mock_py_debugger_logs = [] 
        self.__controller_callbacks = callbacks
        mock_py_debugger_logs.append("initialize")

    def set_code(self, code: str) -> None:
        mock_py_debugger_logs.append("set_code")

    def add_breakpoint(self, line_number: int, cond: str) -> None:
        mock_py_debugger_logs.append(f"add_breakpoint {line_number} {cond}")

    def del_breakpoint(self, line_number: int) -> None:
        mock_py_debugger_logs.append(f"del_breakpoint {line_number}")

    def step_into(self) -> None:
        mock_py_debugger_logs.append("step_into")
        self.__controller_callbacks.execution_paused(self.vars, 0)

    def forward_step(self) -> None:
        mock_py_debugger_logs.append("forward_step")
        self.__controller_callbacks.execution_paused(self.vars, 0)

    def backward_step(self) -> None:
        mock_py_debugger_logs.append("backward_step")
        self.__controller_callbacks.execution_paused(self.vars, 0)

    def do_continue(self) -> None:
        mock_py_debugger_logs.append("do_continue")
        self.__controller_callbacks.execution_paused(self.vars, 0)
    
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

    def test___get_ui_vars(self):
        # Test case 1 : 1 frame
        controller = Controller(MockPyDebugger, MockUICallbacks())
        frames = [{"globals": {"a": 1, "b": 2}, "locals": {"a": 1, "b": 2}}]
        context = MockDebugContext.list_from_frame(frames)
        transfer_vars = controller._Controller__get_ui_vars(context)
        assert transfer_vars.variables[0].description.name == "a"
        assert transfer_vars.variables[0].description.depth == 0
        assert transfer_vars.variables[0].value == 1
        assert transfer_vars.variables[1].description.name == "b"
        assert transfer_vars.variables[1].description.depth == 0
        assert transfer_vars.variables[1].value == 2

        # Test case 2 : 2 frame
        controller = Controller(MockPyDebugger, MockUICallbacks())
        frames = [{"globals": {"a": 1, "b": 2}, "locals": {"c": "Hello", "d": "World"}}, 
                  {"globals": {"a": 1, "b": 2}, "locals": {"a": 1, "b": 2}}]
        context = MockDebugContext.list_from_frame(frames)
        transfer_vars = controller._Controller__get_ui_vars(context)
        assert transfer_vars.variables[0].description.name == "a"
        assert transfer_vars.variables[0].description.depth == 0
        assert transfer_vars.variables[0].value == 1
        assert transfer_vars.variables[1].description.name == "b"
        assert transfer_vars.variables[1].description.depth == 0
        assert transfer_vars.variables[1].value == 2
        assert transfer_vars.variables[2].description.name == "c"
        assert transfer_vars.variables[2].description.depth == 1
        assert transfer_vars.variables[2].value == "Hello"
        assert transfer_vars.variables[3].description.name == "d"
        assert transfer_vars.variables[3].description.depth == 1
        assert transfer_vars.variables[3].value == "World"

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