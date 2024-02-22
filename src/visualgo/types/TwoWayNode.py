""":demand: F1.8"""

from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class TwoWayNode(Node):
    def __init__(self, value: T = None, previous_node: Optional['TwoWayNode'] = None,
                 next_node: Optional['TwoWayNode'] = None):
        super().__init__(value, next_node)
        self.__previous = previous_node

    def has_previous(self) -> bool:
        """
        Checks if this TwoWayNode has a preceding TwoWayNode.
        :return:
        """
        return self.previous() is not None

    def previous(self) -> Optional['TwoWayNode']:
        """
        Returns the preceding TwoWayNode.
        :return: TwoWayNode
        """
        return self.__previous

    def set_previous(self, two_way_node: Optional['TwoWayNode']) -> None:
        """
        Sets the preceding TwoWayNode.
        :param two_way_node: TwoWayNode
        :return: None
        """
        self.__previous = two_way_node
