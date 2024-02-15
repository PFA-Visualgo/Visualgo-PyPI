from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class Stack:
    def push(self, value: T = None) -> None:
        """
        Pushes a value on the top of the stack.
        :param value: Any object
        :return: None
        """
        pass

    def pop(self) -> Optional['T']:
        """
        Removes the top of the stack and returns it.
        :return: The top value of the stack of any type
        """
        pass

    def top(self) -> Optional['T']:
        """
        Returns the top of the stack.
        :return: The top value of the stack of any type
        """
        pass

    def is_empty(self) -> bool:
        """
        Indicates whether the stack is empty.
        :return: A boolean
        """
        return self.__top.next() is None

    def __str__(self) -> str:
        pass
