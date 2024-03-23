import os
from typing import Any

from ..comm_api import from_worker
from .python_thread_shared_worker_data import set_worker_message_value, get_event, get_main_message_value
import signal


class PythonFromWorker(from_worker.FromWorker):
    def send_message(self, mes_id: str, data):
        set_worker_message_value(mes_id, data)
        signal.raise_signal(signal.SIGUSR1)
        # os.sched_yield()
        # get_message_handler()(mes_id, data)

    def wait_for_main_message(self) -> (str, Any):
        get_event().wait()
        get_event().clear()
        return get_main_message_value()
