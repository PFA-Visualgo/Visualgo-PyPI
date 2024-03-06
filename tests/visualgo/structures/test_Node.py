""":demand: F1.8"""

import unittest
from visualgo.structures import Node


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

        self.assertEqual(node.value, None)
        self.assertEqual(node.next, None)

        self.assertEqual(node2.value, 3)
        self.assertEqual(node2.next, node)

        self.assertEqual(node3.value, node)
        self.assertEqual(node3.next, node2)
        self.assertEqual(node3.next.next, node)

        self.assertEqual(node4.value, [13])

    def test_set(self):
        """
        Tests the value assignment of a node :
        -Different types of value
        -The child is not altered
        """
        node = Node()
        self.assertEqual(node.value, None)
        node.set_value(4)
        self.assertEqual(node.value, 4)
        node2 = Node(9)
        self.assertEqual(node2.next, None)
        node2.set_next(node)
        self.assertEqual(node2.next, node)
        node.set_value(90)
        self.assertEqual(node.value, 90)

    def test_has_next(self):
        """
        Tests the has_next method
        """
        node = Node()
        self.assertEqual(node.has_next(), False)

        node2 = Node("h", node)
        self.assertEqual(node2.has_next(), True)


if __name__ == '__main__':
    unittest.main()
