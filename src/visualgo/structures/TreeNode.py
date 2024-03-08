""":demand: F1.8"""
from collections.abc import Iterable
from typing import Optional, TypeVar

from .DoublyLinkedList import DoublyLinkedList
from .Node import Node
T = TypeVar('T')


class TreeNode:

    def __init__(self, value: T = None, children: Iterable = None) -> None:
        self.__value = value
        self.__children = DoublyLinkedList(children)

    def has_child(self) -> bool:
        """
        Tells if this TreeNode has at least one child TreeNode.
        :return: bool
        """
        return not self.__children.is_empty()

    @property
    def children(self):
        """
        Returns the children of this TreeNode.
        :return: List[TreeNode]
        """
        return self.__children

    @property
    def value(self) -> T:  # TODO: Changer nom dans le diagramme et le cahier des charges.
        """
        Returns the value of the TreeNode.
        :return: Object
        """
        return self.__value

    @value.setter
    def value(self, e: T) -> None:  # TODO: Changer nom dans le diagramme et le cahier des charges.
        """
        Sets the value of this TreeNode.
        :param e: Object
        :return: None
        """
        self.__value = e

    def add_child(self, tree_node: Optional['TreeNode']) -> None:
        """
        Adds a child TreeNode to the TreeNode.
        :param tree_node:
        :return:
        """
        self.__children.insert_last(tree_node)

    def delete_child(self, tree_node: Optional['TreeNode']) -> None:
        """
        Deletes a child TreeNode from this TreeNode.
        :param tree_node:
        :return:
        """
        current_node: Node = self.__children.head
        index: int = 0
        while current_node is not tree_node and not current_node.is_sentinel():
            current_node = current_node.next
            index += 1
        if current_node is tree_node:
            self.__children.delete(index)
            return
        raise ValueError("No such child")
