""":demand: F1.8"""

from typing import Optional, TypeVar
from .Node import Node

T = TypeVar('T')


class TwoWayNode(Node):
    """
    A node that can be linked to the preceding node.
    """

    def __init__(self, value: T = None, previous_node: Optional['TwoWayNode'] = None,
                 next_node: Optional['TwoWayNode'] = None):
        super().__init__(value, next_node)
        self._previous = previous_node

    @property
    def previous(self) -> Optional['TwoWayNode']:
        """
        Returns the preceding TwoWayNode.

        :return: TwoWayNode
        """
        return self._previous

    @previous.setter
    def previous(self, two_way_node: Optional['TwoWayNode']) -> None:
        """
        Sets the preceding TwoWayNode.

        :param two_way_node: TwoWayNode
        :return: None
        """
        self._previous = two_way_node

    def has_previous(self) -> bool:
        """
        Checks if this TwoWayNode has a preceding TwoWayNode.

        :return:
        """
        return self.previous is not None

    @classmethod
    def sentinel(cls) -> Optional['TwoWayNode']:
        """
        Creates a sentinel Node.

        :return: Node
        """
        return TwoWayNode()

    def is_sentinel(self):
        """
        Checks if the node is a sentinel.

        :return: bool
        """
        return self.value is None and self.next is None


def TwoWayNode_value(node: TwoWayNode) -> T:
    return node.value


def TwoWayNode_set_value(node: TwoWayNode, value: T) -> None:
    node.value = value


def TwoWayNode_next(node: TwoWayNode) -> Optional[Node]:
    return node.next


def TwoWayNode_set_next(node: TwoWayNode, next: Node) -> Optional[Node]:
    node.next = next


def TwoWayNode_has_next(node: TwoWayNode) -> bool:
    return node.has_next()


def TwoWayNode_sentinel() -> TwoWayNode:
    return TwoWayNode.sentinel()


def TwoWayNode_is_sentinel(node: TwoWayNode) -> bool:
    return node.is_sentinel()


def TwoWayNode_previous(node: TwoWayNode) -> Optional[Node]:
    return node.previous


def TwoWayNode_set_previous(node: TwoWayNode, previous: Node) -> Optional[Node]:
    node.previous = previous


def TwoWayNode_has_previous(node: TwoWayNode) -> bool:
    return node.has_previous()
