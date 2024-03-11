""":demand: F1.8"""

from typing import TypeVar

T = TypeVar('T')


class List:

    def __init__(self, items: list[T] = None) -> None:
        if items is None:
            self.__items: list[T] = []
        else:
            self.__items = items.copy()

    @property
    def length(self) -> int:
        """
        Returns the length of the list.

        :return: int
        """
        return len(self.__items)

    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.

        :param index: int
        :return: Object
        """
        if index < 0 or index >= len(self.__items):
            raise IndexError
        return self.__items[index]

    def insert(self, index: int, e: T) -> None:
        """
        Inserts the element after the given `index`.

        :param index: int
        :param e: Object
        :return: None
        """
        if index < 0 or index >= len(self.__items):
            raise IndexError
        self.__items.insert(index, e)

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.

        :param index: int
        :return: None
        """
        if index < 0 or index >= len(self.__items):
            raise IndexError
        self.__items.pop(index)

    def __str__(self) -> str:
        return self.__items.__str__()
