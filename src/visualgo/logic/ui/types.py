import typing
from dataclasses import dataclass

from ..types import Statistics, SymbolDescription
from . import CodeError

TransferVariableValue = typing.Union[str, int, float, bool, typing.List[NodeType], GraphType] # TODO: continue here add NodeType, GraphType, etc.

@dataclass
class TransferVariable:
    description: SymbolDescription
    type: str
    value: TransferVariableValue

@dataclass
class TransferVariables:
    variables: typing.List[TransferVariable]