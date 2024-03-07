import threading
from typing import Callable, Any

ev: threading.Event
message_value: [str, Any]
worker_thread: threading.Thread
message_handler: Callable[[str, Any], None]


def get_message_value():
    return message_value


def get_event() -> threading.Event:
    return ev


def get_message_handler() -> Callable[[str, Any], None]:
    return message_handler


def start_worker_task(task: Callable[[], None]) -> None:
    global ev, worker_thread
    ev = threading.Event()
    worker_thread = threading.Thread(target=task)
    worker_thread.start()


def set_message_handler(func: Callable[[str, Any], None]):
    global message_handler
    message_handler = func


def send_message(mes_id: str, data: Any) -> None:
    global message_value
    message_value = (mes_id, data)
    ev.set()
