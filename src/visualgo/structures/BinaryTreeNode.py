""":demand: F1.8"""

from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class BinaryTreeNode:
    """
    A node that can be linked to two other nodes.
    """
    def __init__(self, value: Optional[T] = None, left_child: Optional[Node] = None,
                 right_child: Optional[Node] = None):
        self._value = value
        self._left_child = left_child
        self._right_child = right_child

    @property
    def left_child(self) -> Optional['BinaryTreeNode']:
        """
        Returns the left child of this node. Can be None.

        :return: BinaryTreeNode
        """
        return self._left_child

    @left_child.setter
    def left_child(self, binary_tree_node: Optional['BinaryTreeNode']) -> None:
        """
        Sets the left child of this node.

        :param binary_tree_node: The new left child.
        :return: None
        """
        self._left_child = binary_tree_node

    @property
    def right_child(self) -> Optional['BinaryTreeNode']:
        """
        Returns the right child of this node. Can be None.

        :return: BinaryTreeNode
        """
        return self._right_child

    @right_child.setter
    def right_child(self, binary_tree_node: Optional['BinaryTreeNode']) -> None:
        """
        Sets the right child of this node.

        :param binary_tree_node: The new right child.
        :return: None
        """
        self._right_child = binary_tree_node

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
        return self._left_child is not None or self._right_child is not None
