import typing
from dataclasses import dataclass

from ..types import Statistics, SymbolDescription, CodeError


@dataclass
class TransferVariable:
    description: SymbolDescription
    value: typing.Any


@dataclass
class TransferVariables:
    variables: typing.List[TransferVariable]
