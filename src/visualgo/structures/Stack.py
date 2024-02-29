""":demand: F1.8"""

from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class Stack:
    def __init__(self):
        self._top = Node()

    def push(self, value: T = None) -> None:
        """
        Pushes a value on the top of the stack.
        :param value: Any object
        :return: None
        """
        self._top = Node(value, self._top)

    def pop(self) -> Optional['T']:
        """
        Removes the top of the stack and returns it.
        :return: The top value of the stack of any type
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        val: T = self._top.content
        self._top = self._top.next
        return val

    def top(self) -> Optional['T']:
        """
        Returns the top of the stack.
        :return: The top value of the stack of any type
        """
        return self._top

    def is_empty(self) -> bool:
        """
        Indicates whether the stack is empty.
        :return: A boolean
        """
        return self._top.next is None

    def __str__(self) -> str:
        if self._top.next is None:
            return "[ "
        current_node = self._top
        string: str = ""
        while current_node.next is not None:
            string = str(current_node.content) + " " + string
            current_node = current_node.next
        return "[ " + string
