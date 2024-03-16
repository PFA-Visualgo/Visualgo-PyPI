""":demand: F1.8"""

import unittest
from visualgo.structures.TreeNode import *


class TestTreeNode(unittest.TestCase):
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

        self.assertIsNone(node.value)
        self.assertTrue(node.is_sentinel())

        self.assertEqual(node2.value, 3)
        self.assertEqual(node2.children[0], node)

        self.assertEqual(node3.value, node)
        self.assertEqual(node3.children[0], node)
        self.assertEqual(node3.children[1], node2)
        self.assertEqual(TreeNode_children(node3)[1].children[0], node)

        self.assertEqual(node4.value, [13])

        TreeNode_next(node)
        TreeNode_has_next(node)
        TreeNode_set_next(node, node)
        self.assertTrue(TreeNode_is_sentinel(TreeNode_sentinel()))

    def test_children(self):
        """
        Tests the `children` attribute.
        """
        node = TreeNode()
        self.assertTrue(node.children.is_empty())
        node2 = TreeNode(3, [node])
        self.assertTrue(node2.children[0], node)
        node3 = TreeNode("e", [node, node2])
        self.assertTrue(node3.children[0], node)
        self.assertTrue(node3.children[1], node2)

    def test_value(self):
        """
        Tests the assignment of a value.
        """
        node = TreeNode()
        node.value = 1
        self.assertEqual(node.value, 1)
        node.value = "123"
        self.assertEqual(node.value, "123")
        node2 = TreeNode(9, [node])
        self.assertEqual(TreeNode_value(node2), 9)
        TreeNode_set_value(node2, node2)
        self.assertEqual(node2.value, node2)
        self.assertEqual(node2.children[0], node)

    def test_has_child(self):
        """
        Tests the `has_child` method.
        """
        node = TreeNode()
        self.assertFalse(node.has_child())
        node2 = TreeNode(3, [node])
        self.assertTrue(TreeNode_has_child(node2))

    def test_add_child(self):
        """
        Tests the `add_child` method.
        """
        node = TreeNode()
        self.assertTrue(node.children.is_empty())
        node2 = TreeNode(3)
        node.add_child(node2)
        self.assertTrue(node.has_child())
        self.assertEqual(node.children[0], node2)
        self.assertRaises(IndexError, lambda: node.children[1])
        node3 = TreeNode("e", [node, node2])
        TreeNode_add_child(node, node3)
        self.assertEqual(node.children[0], node2)
        self.assertEqual(node.children[1], node3)
        self.assertTrue(node.has_child())
        self.assertRaises(IndexError, lambda: node.children[2])

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
        print(node2.children)
        TreeNode_delete_child(node2, node2)

        self.assertTrue(node2.has_child)
        self.assertEqual(node2.children[0], node)
        self.assertRaises(ValueError, lambda: node2.delete_child(node2))



if __name__ == '__main__':
    unittest.main()
