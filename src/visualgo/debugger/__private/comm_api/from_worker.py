from typing import Any, Callable
from .to_worker import get_message_handler, get_event, get_message_value


def send_message(mes_id: str, data):
    get_message_handler()(mes_id, data)


def wait_for_main_message() -> (str, Any):
    get_event().wait()
    get_event().clear()
    return get_message_value()
