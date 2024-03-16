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


def TreeNode_value(node: TreeNode) -> T:
    return node.value


def TreeNode_set_value(node: TreeNode, value: T) -> None:
    node.value = value


def TreeNode_next(node: TreeNode) -> Optional[Node]:
    return print("Don't use this function ! Use TreeNode_child instead.")


def TreeNode_set_next(node: TreeNode, next: Node) -> Optional[Node]:
    return print("Don't use this function ! Use TreeNode_add_child or TreeNode_delete_child instead.")


def TreeNode_has_next(node: TreeNode) -> bool:
    return print("Don't use this function ! Use TreeNode_has_child instead.") is not None


def TreeNode_sentinel() -> TreeNode:
    return TreeNode.sentinel()


def TreeNode_is_sentinel(node: TreeNode) -> bool:
    return node.is_sentinel()


def TreeNode_children(node: TreeNode) -> DoublyLinkedList:
    return node.children


def TreeNode_has_child(node: TreeNode) -> bool:
    return node.has_child()


def TreeNode_add_child(node: TreeNode, child: Node) -> None:
    return node.add_child(child)


def TreeNode_delete_child(node: TreeNode, child: Node) -> None:
    return node.delete_child(child)
