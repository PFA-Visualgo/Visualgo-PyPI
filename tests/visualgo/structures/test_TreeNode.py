""":demand: F1.8"""

import unittest
from visualgo.structures import TreeNode


class TestNode(unittest.TestCase):
    def test_creation(self):
        """
        Tests the creation of nodes :
        -Empty node
        -TreeNode with child
        -TreeNode with a node as value
        -TreeNode without child but with value
        """
        node = TreeNode()  # Empty node
        node2 = TreeNode(3, [node])  # Parent node
        node3 = TreeNode(node, [node, node2])  # TreeNode containing `node` and parent of `node2` and `node`
        node4 = TreeNode([13])

        self.assertEqual(node.value, None)
        self.assertEqual(node.next, None)

        self.assertEqual(node2.value, 3)
        self.assertEqual(node2.children[0], node)

        self.assertEqual(node3.value, node)
        self.assertEqual(node3.children[0], node2)
        self.assertEqual(node3.children[1], node)
        self.assertEqual(node3.children[0].children[0], node)

        self.assertEqual(node4.value, [13])

    def test_has_child(self):
        """
        Tests the `has_child` method.
        """
        node = TreeNode()
        self.assertFalse(node.has_child)
        node2 = TreeNode(3, [node])
        self.assertTrue(node2.has_child)

    def test_children(self):
        """
        Tests the `children` method.
        """
        node = TreeNode()
        self.assertIsNone(node.children)
        node2 = TreeNode(3, [node])
        self.assertTrue(node2.children[0], node)
        node3 = TreeNode("e", [node, node2])
        self.assertTrue(node3.children[0], node)
        self.assertTrue(node3.children[1], node2)

    def test_add_child(self):
        """
        Tests the `add_child` method.
        """
        node = TreeNode()
        self.assertIsNone(node.children)
        node2 = TreeNode(3)
        node.add_child(node2)
        self.assertTrue(node.has_child)
        self.assertEqual(node.children[0], node2)
        self.assertRaises(IndexError, node.children[1])
        node3 = TreeNode("e", [node, node2])
        node.add_child(node3)
        self.assertEqual(node.children[0], node2)
        self.assertEqual(node.children[1], node3)
        self.assertTrue(node.has_child)
        self.assertRaises(IndexError, node.children[2])

    def test_value(self):
        """
        Tests the `value` method.
        """
        node = TreeNode()
        self.assertIsNone(node.value)
        node.set_value(4)
        self.assertEqual(node.value, 4)
        node2 = TreeNode(9)
        self.assertIsNone(node2.children)
        node2.set_next(node)
        self.assertEqual(node2.children[0], node)
        node.set_value(90)
        self.assertEqual(node.value, 90)

    def test_delete_child(self):
        """
        Tests the `delete_child` method.
        """
        node = TreeNode()
        self.assertRaises(ValueError, lambda: node.delete_child(node))
        node2 = TreeNode(3, [node])
        node2.delete_child(node)
        self.assertFalse(node2.has_child())

        node2.add_child(node)
        node2.add_child(node2)
        node2.delete_child(node2)

        self.assertTrue(node2.has_child)
        self.assertEqual(node2.children[0], node)

    def test_set_value(self):
        """
        Tests the set_value method.
        """
        node = TreeNode()
        node.set_value(1)
        self.assertEqual(node.value, 1)
        node.set_value("123")
        self.assertEqual(node.value, "123")
        node2 = TreeNode(9, [node])
        self.assertEqual(node2.value, 9)
        node2.set_value(node2)
        self.assertEqual(node2.value, node2)
        self.assertEqual(node2.children[0], node)


if __name__ == '__main__':
    unittest.main()
