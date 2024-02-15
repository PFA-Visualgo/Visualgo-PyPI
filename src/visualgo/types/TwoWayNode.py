from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class TwoWayNode(Node):
    def has_previous(self) -> bool:
        """
        Checks if this TwoWayNode has a preceding TwoWayNode.
        :return:
        """
        pass

    def previous(self) -> Optional['TwoWayNode']:
        """
        Returns the preceding TwoWayNode.
        :return: TwoWayNode
        """
        pass

    def set_previous(self, two_way_node: Optional['TwoWayNode']) -> None:
        """
        Sets the preceding TwoWayNode.
        :param two_way_node: TwoWayNode
        :return: None
        """
        pass
