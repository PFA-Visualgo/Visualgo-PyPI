from abc import ABC, abstractmethod

from .debug_types import DebugContext


class DebuggerCallbacksInterface(ABC):

    @abstractmethod
    def on_backward_step_done(
            self, vars: DebugContext, line_number: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_forward_step_done(
            self, vars: DebugContext, line_number: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_step_into_done(self, vars: DebugContext, line_number: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_continue_done(self, vars: DebugContext, line_number: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_stop(self, vars: DebugContext, line_number: int) -> None:
        raise NotImplementedError
