import typing
from dataclasses import dataclass
from enum import Enum

class ExecutionState(Enum):
    NOT_INITIALIZED = "Not Initialized"
    RUNNING = "Running"
    STOPPED = "Stopped"
    FINISHED = "Finished"

TransferVariableValue = typing.Union[str, int, float, bool, typing.List[NodeType], GraphType] # TODO: continue here

@dataclass
class SymboleDescription:
    name: str
    depth: int

@dataclass
class TransferVariable:
    description: SymboleDescription
    type: str
    value: TransferVariableValue

@dataclass
class TransferVariables:
    variables: typing.List[typing.Tuple[str, str]]

@dataclass
class CodeError:
    error_happened: bool # TODO: modify UML
    line: int
    message: str