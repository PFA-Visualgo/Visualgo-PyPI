from dataclasses import dataclass
from inspect import isfunction
from types import FrameType
import re
from typing import Any

_builtin_pattern = re.compile('__.*__')


def _remove_builtins(d):
    return dict(filter(lambda k: not _builtin_pattern.match(k[0]), d.items()))


def _remove_unpickable(d):
    return dict(filter(lambda v: not isfunction(v[1]), d.items()))


_DEFAULT_GLOBALS = {"__file__", "__name__", "__builtins__"}


@dataclass(frozen=True)
class DebugVariables:
    globals: dict[str, Any]
    locals: dict[str, Any]


class DebugContext:
    @classmethod
    def list_from_frame(cls, frame: FrameType, botframe: FrameType) -> list["DebugContext"]:
        """
        Creates a stack of DebugContext, going from `frame` to `botframe` (the debugger's frame)
        :param frame: The top-level frame
        :param botframe: The debugger's frame
        :return: A stack of DebugContext
        """
        lst = []
        cur_frame = frame
        while cur_frame is not None and cur_frame is not botframe:  # Dirty hack to remove all the nasty bdb clutter
            lst.append(cls(cur_frame))
            cur_frame = cur_frame.f_back
        return lst

    def __init__(self, frame: FrameType):
        self.filepath = frame.f_globals["__file__"]
        self.lineno = frame.f_lineno
        self.variables = DebugVariables(_remove_unpickable(_remove_builtins(frame.f_globals)),
                                        _remove_unpickable(_remove_builtins(frame.f_locals)))
        self.function_name = frame.f_code.co_name if frame.f_code.co_name else "<lambda>"

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
