from typing import Optional, TypeVar
from .Table import Table

T = TypeVar('T')


class TreeNode:
    def has_child(self) -> bool:
        """
        Tells if this TreeNode has at least one child TreeNode.
        :return: bool
        """
        pass

    def get_children(self) -> Table:
        """
        Returns the children of this TreeNode.
        :return: List[TreeNode]
        """
        pass

    def get_value(self) -> T:  # TODO: Changer nom dans le diagramme et le cahier des charges.
        """
        Returns the value of the TreeNode.
        :return: Object
        """
        pass

    def add_child(self, tree_node: Optional['TreeNode']) -> None:
        """
        Adds a child TreeNode to the TreeNode.
        :param tree_node:
        :return:
        """
        pass

    def delete_child(self, tree_node: Optional['TreeNode']) -> None:
        """
        Deletes a child TreeNode from this TreeNode.
        :param tree_node:
        :return:
        """
        pass

    def set_value(self, e: T) -> None:  # TODO: Changer nom dans le diagramme et le cahier des charges.
        """
        Sets the value of this TreeNode.
        :param e: Object
        :return: None
        """
        pass
