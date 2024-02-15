from typing import TypeVar

from . import LinkedList
from .TwoWayNode import TwoWayNode

T = TypeVar('T')


class DoublyLinkedList(LinkedList):
    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.
        :param index: int
        :return: Object
        """
        pass

    def get_node(self, index: int) -> TwoWayNode:
        """
        Returns the node at the `index` position.
        :param index: int
        :return: TwoWayNode
        """
        pass

    def get_head(self) -> TwoWayNode:
        """
        Returns the head node of the list.
        :return: TwoWayNode
        """
        pass

    def get_last(self) -> TwoWayNode:
        """
        Returns the last node of the list.
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

    def insert_last(self, e: T) -> None:
        """
        Inserts the element at the last node of the list.
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

    def insert_before(self, index: int, e: T) -> None:
        """
        Inserts the element before the given `index`.
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
