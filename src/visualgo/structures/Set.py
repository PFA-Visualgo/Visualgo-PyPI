from typing import TypeVar

T = TypeVar('T')


class Set:
    def __init__(self, *elements) -> None:
        if len(elements) == 0:
            self.__set = set()
        self.__set = set(elements)

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
