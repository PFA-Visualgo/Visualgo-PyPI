import threading
import typing
from typing import Callable, Any

if typing.TYPE_CHECKING:
    from .python_to_worker import PythonToWorker
my_impl: "PythonToWorker"


def set_impl(impl: "PythonToWorker") -> None:
    global my_impl
    my_impl = impl


def get_message_value():
    return my_impl.message_value


def get_event() -> threading.Event:
    return my_impl.ev


def get_message_handler() -> Callable[[str, Any], None]:
    return my_impl.message_handler
