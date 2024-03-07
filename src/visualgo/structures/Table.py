""":demand: F1.8"""

from typing import TypeVar

T = TypeVar('T')


class Table:

    def __init__(self, size: int) -> None:
        self.__table = [None for _ in range(size)]
        self.__size = size

    def get(self, index: int) -> T:
        """
        Returns the value at the `index` position.
        :param index: int
        :return: Object
        """
        return self.__table[index]

    def set(self, index: int, e: T) -> None:
        """
        Sets the value at the `index` position.
        :param index: int
        :param e: Object
        :return: None
        """
        self.__table[index] = e

    def length(self) -> int:
        """
        Returns the length of the Table.
        :return: int
        """
        return self.__size
