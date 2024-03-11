from dataclasses import dataclass


@dataclass
class Statistics:
    """
    Statistics for the UI.
    
    :demand: F.1.5
    """
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
