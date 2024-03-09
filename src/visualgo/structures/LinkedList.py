""":demand: F1.8"""
from collections.abc import Iterable
from typing import TypeVar
from .Node import Node

T = TypeVar('T')


class LinkedList:
    # head -> ... -> ... -> ... -> sentinel()
    def __init__(self, it: Iterable[T] = None) -> None:
        self.__head: Node = Node.sentinel()
        self.__length: int = 0
        if it is not None:
            for item in it[::-1]:
                self.insert_head(item)

    @property
    def head(self) -> Node:
        """
        Returns the head value of the list.
        :return: TwoWayNode
        """
        return self.__head.value

    @property
    def length(self) -> int:
        """
        Returns the length of the list.
        :return: int
        """
        return self.__length

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        :return: bool
        """
        return self.length == 0

    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.
        :param index: int
        :return: Object
        """
        return self._get_node(index).value

    def _get_node(self, index: int) -> Node:
        """
        Returns the node at the `index` position.
        :param index: int
        :return: TwoWayNode
        """
        if index < 0 or index >= self.length:
            raise IndexError('Index out of range')
        i: int = 0
        current_node = self.__head
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node

    def set(self, index: int, e: T) -> None:
        """
        Sets the element at the `index` position as `e`.
        :param index: int
        :param e: Object
        :return: None
        """
        node: T = self._get_node(index)
        node.value = e

    def insert_head(self, e: T) -> None:
        """
        Inserts the element at the head of the list.
        :param e: Object
        :return: None
        """
        new_node = Node(e, self.__head)
        self.__head = new_node
        self.__length += 1

    def insert_after(self, index: int, e: T) -> None:
        """
        Inserts the element after the given `index`.
        :param index: int
        :param e: Object
        :return: None
        """
        if 0 < index or index > self.__length:
            raise IndexError('Index out of range')
        new_node = Node(e)
        current_node = self._get_node(index)
        new_node.next = current_node.next
        current_node.next = new_node
        self.__length += 1

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.
        :param index: int
        :return: None
        """
        if index < 0 or index >= self.__length:
            raise IndexError('Index out of range')
        self.__length -= 1
        if index == 0:
            self.__head = self.__head.next
            return
        current_node = self._get_node(index - 1)
        current_node.next = current_node.next.next

    def __str__(self):
        if self.is_empty():
            return "[]"
        current_node = self.__head
        string: str = "[{}".format(current_node.value)

        while current_node.has_next():
            current_node = current_node.next
            if current_node.has_next():
                string += "->{}".format(current_node.value)
        return string + "]"

    def __getitem__(self, item: int) -> Node:
        return self.get(item)
