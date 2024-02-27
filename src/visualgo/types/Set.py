from typing import TypeVar, Optional
from collections.abc import Iterable

T = TypeVar('T')


class Set:
    def __init__(self, it: Optional[Iterable] = None) -> None:
        if it is None:
            self.__set = set()
            return
        self.__set = set(it)

    def is_empty(self) -> bool:
        """
        Checks if the set is empty.
        :return: bool
        """
        return len(self.__set) == 0

    def is_in(self, e: T) -> bool:
        """
        Checks if the element `e` is in the set.
        :param e: Object
        :return: bool
        """
        return e in self.__set

    def add(self, e: T) -> None:
        """
        Adds an element to the set.
        :param e: Object
        :return: None
        """
        self.__set.add(e)

    def delete(self, e: T) -> None:
        """
        Removes an element from the set.
        :param e: Object
        :return: None
        """
        self.__set.remove(e)
