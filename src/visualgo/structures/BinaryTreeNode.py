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
