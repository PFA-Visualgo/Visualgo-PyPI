""":demand: F1.8"""

from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class BinaryTreeNode(Node):
    """
    A node that can be linked to two other nodes.
    """

    def __init__(self, value: Optional[T] = None, left_child: Optional[Node] = None,
                 right_child: Optional[Node] = None):
        super().__init__(value)
        self.__right_child = right_child
        self.__left_child = left_child

    @property
    def left_child(self) -> Optional['Node']:
        """
        Returns the left child of this node. Can be None.

        :return: BinaryTreeNode
        """
        return self.__left_child

    @left_child.setter
    def left_child(self, node: Optional['Node']) -> None:
        """
        Sets the left child of this node.

        :param node: The new left child.
        :return: None
        """
        self.__left_child = node

    @property
    def right_child(self) -> Optional['Node']:
        """
        Returns the right child of this node. Can be None.

        :return: BinaryTreeNode
        """
        return self.__right_child

    @right_child.setter
    def right_child(self, node: Optional['Node']) -> None:
        """
        Sets the right child of this node.

        :param node: The new right child.
        :return: None
        """
        self.__right_child = node

    @property
    def value(self) -> T:
        """
        Returns the value of this node. Can be None.

        :return: Object
        """
        return self._value

    @value.setter
    def value(self, e: T) -> None:
        """
        Sets the value of this node.

        :param e: Object
        :return: T
        """
        self._value = e

    def has_child(self) -> bool:
        """
        Tells if this node has at least one child node.

        :return: bool
        """
        return self.left_child is not None or self.right_child is not None


def BinaryTreeNode_value(node: BinaryTreeNode) -> T:
    return node.value


def BinaryTreeNode_set_value(node: BinaryTreeNode, value: T) -> None:
    node.value = value


def BinaryTreeNode_next(node: BinaryTreeNode) -> Optional[Node]:
    return print("Don't use this function ! Use BinaryTreeNode_right_child instead.")


def BinaryTreeNode_set_next(node: BinaryTreeNode, next: Node) -> Optional[Node]:
    return print("Don't use this function ! Use BinaryTreeNode_set_right_child instead.")


def BinaryTreeNode_has_next(node: BinaryTreeNode) -> bool:
    return print("Don't use this function ! Use BinaryTreeNode_has_child instead.") is not None


def BinaryTreeNode_sentinel() -> BinaryTreeNode:
    return BinaryTreeNode.sentinel()


def BinaryTreeNode_is_sentinel(node: BinaryTreeNode) -> bool:
    return node.is_sentinel()


def BinaryTreeNode_left_child(node: BinaryTreeNode) -> Optional[Node]:
    return node.left_child


def BinaryTreeNode_set_left_child(node: BinaryTreeNode, left_child: Node) -> None:
    node.left_child = left_child


def BinaryTreeNode_right_child(node: BinaryTreeNode) -> Optional['Node']:
    return node.right_child


def BinaryTreeNode_set_right_child(node: BinaryTreeNode, right_child: Node) -> None:
    node.right_child = right_child


def BinaryTreeNode_has_child(node: BinaryTreeNode) -> bool:
    return node.has_child()
