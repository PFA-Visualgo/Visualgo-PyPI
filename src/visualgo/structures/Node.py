""":demand: F1.8"""

from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, value: T = None, next_node: Optional['Node'] = None):
        self.__value = value
        self.__next = next_node

    @property
    def next(self) -> Optional['Node']:
        """
        Returns the node following the current node. Can be None.
        :return: Node object
        """
        return self.__next

    @property
    def value(self) -> Optional[T]:
        """
        Returns the value of the node. Can be None.
        :return: Object
        """
        return self.__value

    def has_next(self) -> bool:
        """
        Indicates whether the node is followed by another node.
        :return: A boolean
        """
        return self.next is not None

    @next.setter
    def next(self, next_node: Optional['Node']) -> None:
        """
        Sets the node following the current node. Can be None.
        :param next_node: Node object
        :return: None
        """
        self.__next = next_node

    @value.setter
    def value(self, value: T) -> None:
        """
        Sets the value of the node. Can be None.
        :param value: Any object
        :return: None
        """
        self.__value = value

    @classmethod
    def sentinel(cls) -> Optional['Node']:
        """
        Creates a sentinel Node.
        :return: Node
        """
        return Node()

    def is_sentinel(self):
        """
        Checks if the node is a sentinel.
        :return: bool
        """
        return self.next is None and self.value is None
