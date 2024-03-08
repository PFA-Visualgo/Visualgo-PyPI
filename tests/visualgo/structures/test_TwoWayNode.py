""":demand: F1.8"""

import unittest
from visualgo.structures import TwoWayNode


class TestTwoWayNode(unittest.TestCase):
    def test_creation(self):
        """
        Tests the creation of nodes :
        -Empty node
        -TwoWayNode with child
        -TwoWayNode with a node as value
        -TwoWayNode without child but with value
        """
        node = TwoWayNode()  # Empty node
        node2 = TwoWayNode(4, next_node=node)  # Parent node
        node3 = TwoWayNode(node, node2, node)  # TwoWayNode containing `node`, parent of `node2` and child of `node`
        node4 = TwoWayNode([193])

        self.assertIsNone(node.value)
        self.assertIsNone(node.next)

        self.assertEqual(node2.value, 4)
        self.assertEqual(node2.next, node)

        self.assertEqual(node3.value, node)
        self.assertEqual(node3.previous, node2)
        self.assertEqual(node3.next, node)

        self.assertEqual(node4.value, [193])

    def test_set_previous(self):
        """
        Tests the `set_previous` method.
        """
        node = TwoWayNode()
        node2 = TwoWayNode()
        self.assertIsNone(node.previous)
        node.previous = node2
        self.assertEqual(node.previous, node2)
        node3 = TwoWayNode(9)
        node.previous = node3
        self.assertEqual(node.previous, node3)

    def test_has_previous(self):
        """
        Tests the `has_next` method.
        """
        node = TwoWayNode()
        self.assertFalse(node.has_previous())
        node2 = TwoWayNode("h", node)
        node.previous = node2
        self.assertEqual(node.previous, node2)
        self.assertTrue(node.has_previous())
        self.assertTrue(node2.has_previous())


if __name__ == '__main__':
    unittest.main()
