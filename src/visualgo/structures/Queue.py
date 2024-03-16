""":demand: F1.8"""

from typing import TypeVar
from .DoublyLinkedList import DoublyLinkedList

T = TypeVar('T')


class Queue:
    def __init__(self) -> None:
        """
        Initializes the queue.
        """
        self.__dll = DoublyLinkedList()

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: bool
        """
        return self.__dll.is_empty()

    def enqueue(self, e: T) -> None:
        """
        Adds an element to the end of the queue.

        :param e: Object
        :return: None
        """
        self.__dll.insert_head(e)

    def dequeue(self) -> T:
        """
        Removes an element from the head of the queue and returns it.

        :return: Object
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            first_in = self.__dll.get(self.__dll.length - 1)
            self.__dll.delete(self.__dll.length - 1)
            return first_in

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.

        :return: str
        """
        return self.__dll.__str__()
