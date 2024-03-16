""":demand: F1.8"""

import unittest
from visualgo.structures.Node import *


class TestNode(unittest.TestCase):
    def test_creation(self):
        """
        Tests the creation of nodes :
        -Empty node
        -Node with child
        -Node with a node as value
        -Node without child but with value
        """
        node = Node()  # Empty node
        node2 = Node(3, node)  # Parent node
        node3 = Node(node, node2)  # Node containing `node` and parent of `node2`
        node4 = Node([13])

        self.assertTrue(node.is_sentinel())

        self.assertEqual(node2.value, 3)
        self.assertEqual(node2.next, node)

        self.assertEqual(node3.value, node)
        self.assertEqual(node3.next, node2)
        self.assertEqual(node3.next.next, node)

        self.assertEqual(node4.value, [13])
        self.assertTrue(Node_is_sentinel(Node_sentinel()))

    def test_has_next(self):
        """
        Tests the has_next method
        """
        node = Node()
        self.assertFalse(node.has_next())

        node2 = Node("h", node)
        self.assertTrue(Node_has_next(node2))

    def test_set(self):
        """
        Tests the value assignment of a node :
        -Different types of value
        -The child is not altered
        """
        node = Node()
        self.assertIsNone(node.value)
        node.value = 4
        self.assertEqual(node.value, 4)
        node2 = Node(9)
        self.assertIsNone(Node_next(node2))
        Node_set_next(node2, node)
        self.assertEqual(node2.next, node)
        Node_set_value(node, 90)
        self.assertEqual(Node_value(node), 90)


if __name__ == '__main__':
    unittest.main()
