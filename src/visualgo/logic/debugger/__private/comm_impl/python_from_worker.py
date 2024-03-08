from typing import Any

from ..comm_api import from_worker
from .python_shared_worker_data import get_message_handler, get_event, get_message_value


class PythonFromWorker(from_worker.FromWorker):
    def send_message(self, mes_id: str, data):
        get_message_handler()(mes_id, data)

    def wait_for_main_message(self) -> (str, Any):
        get_event().wait()
        get_event().clear()
        return get_message_value()
