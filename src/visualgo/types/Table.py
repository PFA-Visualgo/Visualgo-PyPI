from typing import TypeVar

T = TypeVar('T')


class Table:
    def get(self, index: int) -> T:
        """
        Returns the value at the `index` position.
        :param index: int
        :return: Object
        """
        pass

    def set(self, index: int, e: T) -> None:
        """
        Sets the value at the `index` position.
        :param index: int
        :param e: Object
        :return: None
        """
        pass

    def length(self) -> int:
        """
        Returns the length of the Table.
        :return: int
        """
        pass
