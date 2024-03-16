""":demand: F1.8"""

from collections.abc import Iterable
from typing import Optional, TypeVar
from .DoublyLinkedList import DoublyLinkedList
from .Node import Node

T = TypeVar('T')


class TreeNode(Node):
    def __init__(self, value: T = None, children: Iterable = None) -> None:
        super().__init__(value)
        self.__children = DoublyLinkedList(children)

    @property
    def children(self):
        """
        Returns the children of this TreeNode.

        :return: List[TreeNode]
        """
        return self.__children

    """
    @property
    def value(self) -> T:
        \"""
        Returns the value of the TreeNode.

        :return: Object
        \"""
        return self._value

    @value.setter
    def value(self, e: T) -> None:
        \"""
        Sets the value of this TreeNode.

        :param e: Object
        :return: None
        \"""
        self._value = e"""

    def has_child(self) -> bool:
        """
        Tells if this TreeNode has at least one child TreeNode.

        :return: bool
        """
        return not self.__children.is_empty()

    def add_child(self, node: Optional['Node']) -> None:
        """
        Adds a child TreeNode to the TreeNode.

        :param node:
        :return:
        """
        self.__children.insert_last(node)

    def delete_child(self, node: Optional['Node']) -> None:
        """
        Deletes a child TreeNode from this TreeNode.

        :param node:
        :return:
        """
        if self.children.is_empty():
            raise ValueError("The node has no child.")
        index: int = 0
        for current_node in self.children:
            if current_node is node:
                return self.children.delete(index)
            index += 1
        raise ValueError("No such child")

    def is_sentinel(self) -> bool:
        """
        Checks if the node is a sentinel.

        :return: bool
        """
        return self.children.is_empty() and self.value is None
