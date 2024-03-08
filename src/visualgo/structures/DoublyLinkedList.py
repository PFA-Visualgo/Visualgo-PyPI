""":demand: F1.8"""
from collections.abc import Iterable
from typing import TypeVar

from .Node import Node

from .TwoWayNode import TwoWayNode

T = TypeVar('T')


class DoublyLinkedList:
    # head <=> ... <=> ... <=> ... <=> sentinel()
    def __init__(self, it: Iterable[T] = None) -> None:
        """
        Initializes the doubly linked list.
        """
        self.__head: TwoWayNode = TwoWayNode.sentinel()
        self.__tail: TwoWayNode = self.__head
        self.__length = 0
        if it is not None:
            for item in it:
                self.insert_last(item)

    @property
    def head(self) -> TwoWayNode:
        """
        Returns the head value of the doubly linked list.
        :return: TwoWayNode
        """
        return self.__head.value

    @property
    def length(self) -> int:
        """
        Returns the length of the doubly linked list.
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
        return self.get_node(index).value

    def get_node(self, index: int) -> TwoWayNode:
        """
        Returns the node at the `index` position.
        :param index: int
        :return: TwoWayNode
        """
        if index >= self.length:
            raise IndexError('Index out of range')
        if index < 0:
            raise IndexError('Negative index')
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
        node: T = self.get_node(index)
        node.value = e

    def insert_head(self, e: T) -> None:
        """
        Inserts the element at the head of the list.
        :param e: Object
        :return: None
        """
        new_node = TwoWayNode(e, next_node=self.__head)
        if self.is_empty():
            self.__tail = new_node
        self.__head.previous = new_node
        self.__head = new_node
        self.__length += 1

    def insert_after(self, index: int, e: T) -> None:
        """
        Inserts the element after the given `index`.
        :param index: int
        :param e: Object
        :return: None
        """
        if index == self.__length - 1:
            self.insert_last(e)
            return
        if index < 0 or index >= self.__length:
            raise IndexError('Index out of range')
        else:
            new_node = TwoWayNode(e)
            index_node = self.get_node(index)
            new_node.next = index_node.next
            new_node.previous = index_node
            index_node.next = new_node
            new_node.next.previous = new_node
        self.__length += 1

    def insert_last(self, e: T) -> None:
        """
        Inserts the element at the last node of the list.
        :param e: Object
        :return: None
        """
        if self.is_empty():
            return self.insert_head(e)
        new_node = TwoWayNode(e)
        # last_node = self.get_node(self.__length - 1)
        tmp_sentinel = self.__tail.next
        self.__tail.next = new_node
        new_node.previous = self.__tail
        new_node.next = tmp_sentinel
        self.__tail = new_node
        self.__length += 1

    def insert_before(self, index: int, e: T) -> None:
        """
        Inserts the element before the given `index`.
        :param index: int
        :param e: Object
        :return: None
        """
        if index == 0:
            self.insert_head(e)
            return
        if index == self.__length:
            self.insert_last(e)
            return
        if index < 0 or index > self.__length:
            raise IndexError('Index out of range')
        else:
            new_node = TwoWayNode(e)
            index_node = self.get_node(index)
            index_node.previous.next = new_node
            new_node.next = index_node
            new_node.previous = index_node.previous
            index_node.previous = new_node

        self.__length += 1

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.
        :param index: int
        :return: None
        """
        if index < 0 or index > self.__length:
            raise IndexError('Index out of index')
        if index == 0:
            self.__head = self.__head.next
            self.__head.previous = None
        else:
            current_node = self.get_node(index)
            previous_node = current_node.previous
            previous_node.next = current_node.next
            current_node.next.previous = previous_node
        self.__length -= 1

    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            current_node = self.__head
            result = '['
            while current_node.next:
                result += str(current_node.value) + ' ↔ '
                current_node = current_node.next
            result += str(current_node.value) + ']'
            return result

    def __getitem__(self, index: int) -> Node:
        return self.get(index)
