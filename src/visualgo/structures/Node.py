""":demand: F1.8"""

from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, value: T = None, next_node: Optional['Node'] = None):
        self._value = value
        self.__next = next_node

    @property
    def next(self) -> Optional['Node']:
        """
        Returns the node following the current node. Can be None.

        :return: Node object
        """
        return self.__next

    @next.setter
    def next(self, next_node: Optional['Node']) -> None:
        """
        Sets the node following the current node. Can be None.

        :param next_node: Node object
        :return: None
        """
        self.__next = next_node

    @property
    def value(self) -> Optional[T]:
        """
        Returns the value of the node. Can be None.

        :return: Object
        """
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        """
        Sets the value of the node. Can be None.

        :param value: Any object
        :return: None
        """
        self._value = value

    def has_next(self) -> bool:
        """
        Indicates whether the node is followed by another node.

        :return: A boolean
        """
        return self.next is not None

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


def Node_value(node: Node) -> T:
    return node.value


def Node_set_value(node: Node, value: T) -> None:
    node.value = value


def Node_next(node: Node) -> T:
    return node.next


def Node_set_next(node: Node, next: Optional['Node']) -> T:
    node.next = next


def Node_has_next(node: Node) -> bool:
    return node.has_next()


def Node_sentinel() -> Node:
    return Node.sentinel()


def Node_is_sentinel(node: Node) -> bool:
    return node.is_sentinel()
