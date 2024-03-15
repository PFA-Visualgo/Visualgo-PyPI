""":demand: F1.8"""

from typing import TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class List(ABC):
    @property
    @abstractmethod
    def length(self) -> int:
        """
        Returns the length of the list.

        :return: int
        """

    @abstractmethod
    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.

        :param index: int
        :return: Object
        """

    @abstractmethod
    def insert(self, index: int, e: T) -> None:
        """
        Inserts the element after the given `index`.

        :param index: int
        :param e: Object
        :return: None
        """

    @abstractmethod
    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.

        :param index: int
        :return: None
        """
