""":demand: F1.8"""

from typing import Optional, TypeVar

from .Set import Set

T = TypeVar('T')


class TreeNode:

    def __init__(self, value:T, children:Set) -> None:
        self.__value = value
        self.__children = children


    def has_child(self) -> bool:
        """
        Tells if this TreeNode has at least one child TreeNode.
        :return: bool
        """
        return not self.__children.is_empty()

    def get_children(self) -> Set:
        """
        Returns the children of this TreeNode.
        :return: List[TreeNode]
        """
        return self.__children

    def get_value(self) -> T:  # TODO: Changer nom dans le diagramme et le cahier des charges.
        """
        Returns the value of the TreeNode.
        :return: Object
        """
        return self.__value

    def add_child(self, tree_node: Optional['TreeNode']) -> None:
        """
        Adds a child TreeNode to the TreeNode.
        :param tree_node:
        :return:
        """
        self.__children.add(tree_node)

    def delete_child(self, tree_node: Optional['TreeNode']) -> None:
        """
        Deletes a child TreeNode from this TreeNode.
        :param tree_node:
        :return:
        """
        self.__children.delete(tree_node)

    def set_value(self, e: T) -> None:  # TODO: Changer nom dans le diagramme et le cahier des charges.
        """
        Sets the value of this TreeNode.
        :param e: Object
        :return: None
        """
        self.__value = e
