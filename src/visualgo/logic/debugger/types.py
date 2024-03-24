from inspect import isfunction
from types import FrameType
import re

_builtin_pattern = re.compile('__.*__')


def _remove_builtins(d):
    return dict(filter(lambda k: not _builtin_pattern.match(k[0]), d.items()))


def _remove_unpickable(d):
    return dict(filter(lambda v: not isfunction(v[1]), d.items()))


_DEFAULT_GLOBALS = {"__file__", "__name__", "__builtins__"}


class DebugVariables:
    def __init__(self, glob, loc):
        self.globals = glob
        self.locals = loc

    def __str__(self):
        return str({"globals": self.globals, "locals": self.locals})


class DebugContext:
    def __init__(self, frame: FrameType):
        self.filepath = frame.f_globals["__file__"]
        self.lineno = frame.f_lineno
        self.stack = []
        cur_frame = frame
        while "bdb.py" not in cur_frame.f_globals["__file__"]:  # Dirty hack to remove all the nasty bdb clutter
            self.stack.append(DebugVariables(_remove_unpickable(_remove_builtins(cur_frame.f_globals)),
                                             _remove_unpickable(_remove_builtins(cur_frame.f_locals)))
                              )
            cur_frame = cur_frame.f_back

    def __str__(self):
        return str({"filepath": self.filepath, "lineno": self.lineno,
                    "stack": "[" + ",".join(str(x) for x in self.stack) + "]"})
