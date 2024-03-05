from dataclasses import dataclass


@dataclass
class Statistics:
    function_calls: dict[str, int]


@dataclass
class SymbolDescription:
    name: str
    depth: int


@dataclass
class CodeError:
    error_happened: bool  # TODO: modify UML
    line: int
    message: str
