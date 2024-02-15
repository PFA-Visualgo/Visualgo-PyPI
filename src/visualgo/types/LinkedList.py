from typing import TypeVar
from .Node import Node

T = TypeVar('T')


class LinkedList:
    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        :return: bool
        """
        pass

    def length(self) -> int:
        """
        Returns the length of the list.
        :return: int
        """
        pass

    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.
        :param index: int
        :return: Object
        """
        pass

    def get_node(self, index: int) -> Node:
        """
        Returns the node at the `index` position.
        :param index: int
        :return: TwoWayNode
        """
        pass

    def get_head(self) -> Node:
        """
        Returns the head node of the list.
        :return: TwoWayNode
        """
        pass

    def set(self, index: int, e: T) -> None:
        """
        Sets the element at the `index` position as `e`.
        :param index: int
        :param e: Object
        :return: None
        """
        pass

    def insert_head(self, e: T) -> None:
        """
        Inserts the element at the head of the list.
        :param e: Object
        :return: None
        """
        pass

    def insert_after(self, index: int, e: T) -> None:
        """
        Inserts the element after the given `index`.
        :param index: int
        :param e: Object
        :return: None
        """
        pass

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.
        :param index: int
        :return: None
        """
        pass

    def __str__(self):
        pass
