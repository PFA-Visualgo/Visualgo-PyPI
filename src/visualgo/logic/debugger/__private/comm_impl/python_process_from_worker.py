import os
import signal
from typing import Any

from ..comm_api.from_worker import FromWorker


class PythonProcessFromWorker(FromWorker):

    def __init__(self, pipe_conn, parent_pid):
        self.pipe_conn = pipe_conn
        self.parent_pid = parent_pid

    def send_message(self, mes_id: str, data: Any):
        self.pipe_conn.send((mes_id, data))
        os.kill(self.parent_pid, signal.SIGUSR1)

    def wait_for_main_message(self) -> (str, Any):
        return self.pipe_conn.recv()
