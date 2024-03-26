""":demand: F1.8"""

from .TreeNode import TreeNode

class Tree:
    def __init__(self) -> None:
        self.__root = TreeNode()

    @property
    def root(self) -> TreeNode:
        return self.__root
    
    def __str__(self) -> str:
        return str(self.__root)
