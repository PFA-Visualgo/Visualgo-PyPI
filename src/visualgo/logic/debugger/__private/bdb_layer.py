import bdb
import sys
from sys import stderr
from typing import Any

from ..types import DebugContext
from .comm_api import from_worker

_FILE_NAME = "__visualgo_code.py"


def _run_bdb_task():
    mes_id: str = ""
    mes_data: Any = ""
    while mes_id != "SET_CODE":
        mes_id, mes_data = from_worker.get_implementation().wait_for_main_message()
    dbg = BdbLayer()
    code = mes_data + "\npass"
    lines = code.split("\n")
    CANONIC_FILE_NAME = dbg.canonic(_FILE_NAME)
    with open(CANONIC_FILE_NAME, "w") as f:
        f.write(code)
        f.flush()
        try:
            cmd = compile(code, CANONIC_FILE_NAME, "exec")
            dbg.set_source(code)
            dbg.set_break(CANONIC_FILE_NAME, len(lines))
            dbg.run(cmd, {"__file__": CANONIC_FILE_NAME, "__name__": "__main__"})
        except SyntaxError as e:
            print("Invalid code.")


class BdbLayer(bdb.Bdb):
    def __init__(self, skip=None):
        super().__init__(skip)
        self.lines = None
        self.actions = {
            "SET_CODE": self.do_set_code,
            "CONT": self.do_continue,
            "ADD_BP": self.do_add_breakpoint,
            "DEL_BP": self.do_del_breakpoint,
            "FW_S": self.do_forward_step,
            "BW_S": self.do_backwards_step,
            "FW_N": self.do_forward_next
        }

    def do_add_breakpoint(self, data):
        global _FILE_NAME
        lineno = data[0]
        cond = data[1]
        self.set_break(self.canonic(_FILE_NAME), lineno, cond=cond)
        return False

    def do_del_breakpoint(self, data):
        global _FILE_NAME
        lineno: int = data
        self.clear_break(self.canonic(_FILE_NAME), lineno)
        return False

    def do_forward_step(self, data):
        self.set_step()
        return True

    def do_backwards_step(self, data):
        print("Call to backwards step. It is NOT implemented!", file=stderr)
        return True

    def do_forward_next(self, data):
        print("Call to forward next. It is NOT implemented!", file=stderr)
        # self.set_next()
        return True

    def do_set_code(self, data):
        print("Call to set_code. It is NOT implemented!", file=stderr)
        return True

    def do_continue(self, data):
        self.set_continue()
        return True

    def _cmdloop(self):
        should_exit = False
        while not should_exit:
            mes_id, mes_data = from_worker.get_implementation().wait_for_main_message()
            should_exit = self.actions[mes_id](mes_data)

    def user_line(self, frame):
        if frame.f_lineno == len(self.lines):
            from_worker.get_implementation().send_message("EXEC_DONE", DebugContext.list_from_frame(frame))
        else:
            from_worker.get_implementation().send_message("EXEC_PAUSED", DebugContext.list_from_frame(frame))
            self._cmdloop()

    def user_return(self, frame, return_value):
        pass

    def user_call(self, frame, argument_list):
        pass

    def user_exception(self, frame, exc_info):
        from_worker.get_implementation().send_message("EXEC_THROWED",
                                                      (exc_info[0], DebugContext.list_from_frame(frame)))

    def set_source(self, code: str):
        self.lines = code.split("\n")

    def run(self, cmd, _globals=None, _locals=None):
        try:
            super().run(cmd, _globals, _locals)
        except SystemExit as e:
            pass
        except:
            ex_type, ex, t = sys.exc_info()
            while t.tb_next:
                t = t.tb_next
            frame = t.tb_frame
            from_worker.get_implementation().send_message("EXEC_THROWED",
                                                          (ex_type, DebugContext.list_from_frame(frame)))
