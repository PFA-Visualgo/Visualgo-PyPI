from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def has_next(self) -> bool:
        """
        Indicates whether the node is followed by another node.
        :return: A boolean
        """
        pass

    def next(self) -> Optional['Node']:
        """
        Returns the node following the current node. Can be None.
        :return: Node object
        """
        pass

    def set_next(self, next_node: Optional['Node']) -> None:
        """
        Sets the node following the current node. Can be None.
        :param next_node: Node object
        :return: None
        """
        pass

    def content(self) -> Optional[T]:
        """
        Returns the content of the node. Can be None.
        :return: Object
        """
        pass

    def set_content(self, content: T) -> None:
        """
        Sets the content of the node. Can be None.
        :param content: Any object
        :return: None
        """
        pass

    @classmethod
    def sentinel(cls) -> Optional['Node']:
        """
        Creates a sentinel Node.
        :return: Node
        """
        pass

    def is_sentinel(self):
        """
        Checks if the node is a sentinel.
        :return: bool
        """
        pass
