""":demand: F1.8"""

from typing import TypeVar

T = TypeVar('T')


class List:
    def __init__(self, items: list[T] = None) -> None:
        if items is None:
            self.__items: list[T] = []
        else:
            self.__items = items.copy()

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

    def insert_after(self, index: int,
                     e: T) -> None:  # TODO : Changer nom de la méthode dans le diagramme des classes et cahier des charges
        """
        Inserts the element after the given `index`.
        :param index: int
        :param e: Object
        :return: None
        """
        if index < 0 or index >= len(self.__items):
            raise IndexError
        self.__items.insert(index + 1, e)

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.
        :param index: int
        :return: None
        """
        if index < 0 or index >= len(self.__items):
            raise IndexError
        self.__items.pop(index)
