""":demand: F1.8"""

from typing import TypeVar

from .LinkedList import LinkedList
from .TwoWayNode import TwoWayNode

T = TypeVar('T')


class DoublyLinkedList(LinkedList):
    # head <=> ... <=> ... <=> ... <=> sentinel()
    def __init__(self):
        """
        Initializes the doubly linked list.
        """
        super().__init__()
        self.__head: TwoWayNode = self.head
    
    def insert_head(self, e: T) -> None:
        """
        Inserts the element at the head of the list.
        :param e: Object
        :return: None
        """
        new_node = TwoWayNode(e)
        self.get_head().set_previous(new_node)
        new_node.set_next(self.head)
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
            new_node.set_next(index_node.next())
            new_node.set_previous(index_node)
            index_node.set_next(new_node)
            new_node.next().set_previous(new_node)
        self.__length += 1
    
    def insert_last(self, e: T) -> None:
        """
        Inserts the element at the last node of the list.
        :param e: Object
        :return: None
        """
        new_node = TwoWayNode(e)
        last_node = self.get_node(self.__length - 1)
        last_node.set_next(new_node)
        new_node.set_previous(last_node)
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
        if  index < 0 or index > self.__length:
            raise IndexError('Index out of range')
        else:
            new_node = TwoWayNode(e)
            index_node = self.get_node(index)
            new_node.set_next(index_node)
            new_node.set_previous(index_node.previous())
            index_node.set_previous(new_node)

        self.__length += 1
        
    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.
        :param index: int
        :return: None
        """
        if index < 0 or index >= self.__length:
            raise IndexError('Index out of index')
        self.__length -= 1
        if index == 0:
            self.__head = self.__head.next()
        else:
            current_node = self.get_node(index)
            current_node.previous().set_next(current_node.next())
            current_node.next().set_previous(current_node.previous())
