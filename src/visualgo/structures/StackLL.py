""":demand: F1.8"""

from typing import Optional, TypeVar
from .LinkedList import LinkedList

T = TypeVar('T')


class Stack:
    def __init__(self):
        self.__ll = LinkedList()

    def push(self, value: T = None) -> None:
        """
        Pushes a value on the top of the stack.
        :param value: Any object
        :return: None
        """
        self.__ll.insert_head(value)

    def pop(self) -> Optional['T']:
        """
        Removes the top of the stack and returns it.
        :return: The top value of the stack of any type
        """
        if self.__ll.is_empty():
            raise IndexError("Stack is empty")
        value = self.__ll.head
        self.__ll.delete(0)
        return value

    def top(self) -> Optional['T']:
        """
        Returns the top of the stack.
        :return: The top value of the stack of any type
        """
        return self.__ll.head

    def is_empty(self) -> bool:
        """
        Indicates whether the stack is empty.
        :return: A boolean
        """
        return self.__ll.is_empty()

    def __str__(self) -> str:
        return str(self.__ll)
