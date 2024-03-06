""":demand: F1.8"""

import unittest
from visualgo.structures import BinaryTreeNode


class TestNode(unittest.TestCase):
    def test_creation(self):
        """
        Tests the creation of nodes :
        -Empty node
        -BinaryTreeNode with children
        -BinaryTreeNode with a node as value
        -BinaryTreeNode without child but with value
        """
        node = BinaryTreeNode()  # Empty node
        node2 = BinaryTreeNode(36, node)  # Parent node
        node3 = BinaryTreeNode(node, node, node2)  # BinaryTreeNode containing `node` and parent of `node2` and `node`
        node4 = BinaryTreeNode([13])

        self.assertIsNone(node.value)
        self.assertIsNone(node.right_child)

        self.assertEqual(node2.value, 36)
        self.assertEqual(node2.left_child, node)

        self.assertEqual(node3.value, node)
        self.assertEqual(node3.left_child, node2)
        self.assertEqual(node3.right_child, node)
        self.assertEqual(node3.left_child.left_child, node)

        self.assertEqual(node4.value, [13])

    def test_has_child(self):
        """
        Tests the `has_child` method.
        """
        node = BinaryTreeNode()
        self.assertFalse(node.has_child)
        node2 = BinaryTreeNode(3, node)
        self.assertTrue(node2.has_child)
        node3 = BinaryTreeNode(67, node, node2)
        self.assertTrue(node3.has_child)

    def test_set_left_child(self):
        """
        Tests the `set_left_child` method.
        """
        node = BinaryTreeNode()
        self.assertIsNone(node.left_child)
        node2 = BinaryTreeNode(3, node)
        self.assertEqual(node2.left_child, node)
        node.set_left_child(node2)
        self.assertEqual(node.left_child, node2)
        node2.set_left_child(node)
        self.assertEqual(node2.left_child, node)

    def test_set_right_child(self):
        """
        Tests the `set_right_child` method.
        """
        node = BinaryTreeNode()
        self.assertIsNone(node.right_child)
        node2 = BinaryTreeNode(3, node)
        self.assertEqual(node2.right_child, node)
        node.set_right_child(node2)
        self.assertEqual(node.right_child, node2)
        node2.set_right_child(node)
        self.assertEqual(node2.right_child, node)

    def test_set_value(self):
        """
        Tests the `value` method.
        """
        node = BinaryTreeNode()
        self.assertIsNone(node.value)
        node.set_value(4)
        self.assertEqual(node.value, 4)
        node2 = BinaryTreeNode(9)
        node2.set_right_child(node)
        self.assertEqual(node2.right_child, node)
        node.set_value(90)
        self.assertEqual(node.value, 90)


if __name__ == '__main__':
    unittest.main()
