from typing import List, Optional, TypeVar
from .TreeNode import TreeNode

T = TypeVar('T')


class Tree:
    def __init__(self, value: Optional[T]) -> None:
        self.__root = TreeNode(value)

    @property
    def root(self) -> TreeNode:
        return self.__root

    def add_child(self, parent: TreeNode, child: TreeNode) -> None:
        if parent is None:
            self.__root = child
        else:
            parent.add_child(child)

    def remove_child(self, parent: TreeNode, child: TreeNode) -> None:
        if parent is not None:
            parent.delete_child(child)

    def is_empty(self) -> bool:
        return self.__root is None

    def depth_first_preorder(self) -> List[TreeNode]:
        result = []
        self.__depth_first_preorder_recursive(self.__root, result)
        return result

    def __depth_first_preorder_recursive(self, node: TreeNode, result: List[TreeNode]) -> None:
        if node is None:
            return
        result.append(node)
        for child in node.children:
            self.__depth_first_preorder_recursive(child, result)

    def depth_first_inorder(self) -> List[TreeNode]:
        result = []
        if self.__root is not None:
            self.__depth_first_inorder_recursive(self.__root, result)
        return result

    def __depth_first_inorder_recursive(self, node: TreeNode, result: List[TreeNode]) -> None:
        if node is None:
            return
        for child in node.children:
            self.__depth_first_inorder_recursive(child, result)
        result.append(node)

    def depth_first_postorder(self) -> List[TreeNode]:
        result = []
        self.__depth_first_postorder_recursive(self.__root, result)
        return result

    def __depth_first_postorder_recursive(self, node: TreeNode, result: List[TreeNode]) -> None:
        if node is None:
            return
        for child in node.children:
            self.__depth_first_postorder_recursive(child, result)
        result.append(node)

    def __str__(self):
        pass


def Tree_root(tree: Tree) -> TreeNode:
    return tree.root


def Tree_is_empty(tree: Tree) -> bool:
    return tree.is_empty()


def Tree_depth_first_preorder(tree: Tree) -> List[TreeNode]:
    return tree.depth_first_preorder()


def Tree_depth_first_inorder(tree: Tree) -> List[TreeNode]:
    return tree.depth_first_inorder()


def Tree_depth_first_postorder(tree: Tree) -> List[TreeNode]:
    return tree.depth_first_postorder()
