from typing import TypeVar

T = TypeVar('T')


class Set:
    def is_empty(self) -> bool:
        """
        Checks if the set is empty.
        :return: bool
        """
        pass

    def is_in(self, e: T) -> bool:
        """
        Checks if the element `e` is in the set.
        :param e: Object
        :return: bool
        """
        pass

    def add(self, e: T) -> None:
        """
        Adds an element to the set.
        :param e: Object
        :return: None
        """
        pass

    def delete(self, e: T) -> None:
        """
        Removes an element from the set.
        :param e: Object
        :return: None
        """
        pass

    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.
        :param index: int
        :return: Object
        """
        pass
