from inspect import isfunction
from types import FrameType


def _dict_diff(d1, d2):
    return {k: d1[k] for k in set(d1) - set(d2)}


def _remove_functions(d):
    return dict(filter(lambda v: not isfunction(v[1]), d.items()))


_DEFAULT_GLOBALS = {"__file__", "__name__", "__builtins__"}


class DebugVariables:
    def __init__(self, glob, loc):
        self.globals = glob
        self.locals = loc


class DebugContext:
    def __init__(self, filepath: str, lineno: int, frame: FrameType):
        self.filepath = filepath
        self.lineno = lineno
        self.variables = []
        cur_frame = frame
        while cur_frame is not None:
            self.variables.append(DebugVariables(_remove_functions(_dict_diff(cur_frame.f_globals, _DEFAULT_GLOBALS)),
                                             _dict_diff(cur_frame.f_locals, _DEFAULT_GLOBALS))
                              )
            cur_frame = cur_frame.f_back