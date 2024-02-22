""":demand: F1.8"""

from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, content: T = None, next_node: Optional['Node'] = None):
        self.__content = content
        self.__next = next_node

    def has_next(self) -> bool:
        """
        Indicates whether the node is followed by another node.
        :return: A boolean
        """
        return self.next() is not None

    def next(self) -> Optional['Node']:
        """
        Returns the node following the current node. Can be None.
        :return: Node object
        """
        return self.__next

    def set_next(self, next_node: Optional['Node']) -> None:
        """
        Sets the node following the current node. Can be None.
        :param next_node: Node object
        :return: None
        """
        self.__next = next_node

    def content(self) -> Optional[T]:
        """
        Returns the content of the node. Can be None.
        :return: Object
        """
        return self.__content

    def set_content(self, content: T) -> None:
        """
        Sets the content of the node. Can be None.
        :param content: Any object
        :return: None
        """
        self.__content = content

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
        return self.next() is None and self.content() is None
