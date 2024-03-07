import bdb
from ..debug_context import DebugContext
from .comm_api import from_worker


def init(code_str: str):
    while True:
        mes_id, mes_data = from_worker.wait_for_main_message()
        print(mes_id, mes_data)


class BdbLayer(bdb.Bdb):
    def user_line(self, frame):
        print("User line")
        pass

    def user_return(self, frame, return_value):
        pass

    def user_call(self, frame, argument_list):
        pass

    def user_exception(self, frame, exc_info):
        pass
