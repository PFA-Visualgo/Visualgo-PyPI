""":demand: F1.8"""

from typing import Optional, TypeVar
from .TreeNode import TreeNode

T = TypeVar('T')


class BinaryTreeNode(TreeNode):
    def has_child(self) -> bool:
        """
        Tells if this node has at least one child node.
        :return: bool
        """
        pass

    @property
    def left_child(self) -> Optional['BinaryTreeNode']:
        """
        Returns the left child of this node. Can be None.
        :return: BinaryTreeNode
        """
        pass

    @left_child.setter
    def left_child(self, binary_tree_node: Optional['BinaryTreeNode']) -> None:
        """
        Sets the left child of this node.
        :param binary_tree_node: The new left child.
        :return: None
        """
        pass

    @property
    def right_child(self) -> Optional['BinaryTreeNode']:
        """
        Returns the right child of this node. Can be None.
        :return: BinaryTreeNode
        """
        pass

    @right_child.setter
    def right_child(self, binary_tree_node: Optional['BinaryTreeNode']) -> None:
        """
        Sets the right child of this node.
        :param binary_tree_node: The new right child.
        :return: None
        """
        pass

    @property
    def value(self) -> T:
        """
        Returns the value of this node. Can be None.
        :return: Object
        """
        pass

    @value.setter
    def value(self, e: T) -> None:
        """
        Sets the value of this node.
        :param e: Object
        :return: T
        """
        pass
