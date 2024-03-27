import unittest
from visualgo.structures.Tree import *


class TestTree(unittest.TestCase):
    def test_creation(self):
        tree = Tree()
        self.assertTrue(tree.is_empty())
        tree2 = Tree([90])
        tree3 = Tree("j")
        self.assertFalse(tree2.is_empty())
        self.assertFalse(Tree_is_empty(tree3))
        print(tree, tree2, tree3)

    def test_depth_first_preorder(self):
        self.assertEqual(Tree().depth_first_preorder(), [])
        tree = Tree(1)
        root = tree.root
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        child3 = TreeNode(4)
        root.add_child(child1)
        root.add_child(child2)
        child2.add_child(child3)

        expected_preorder = [root, child1, child2, child3]
        self.assertEqual(Tree_depth_first_preorder(tree), expected_preorder)

    def test_depth_first_inorder(self):
        self.assertEqual(Tree().depth_first_inorder(), [])
        tree = Tree(2)
        root = tree.root
        child1 = TreeNode(1)
        child2 = TreeNode(3)
        child3 = TreeNode(4)
        tree.root.add_child(child1)
        tree.root.add_child(child2)
        child2.add_child(child3)

        expected_inorder = [child1, child3, child2, root]
        self.assertEqual(Tree_depth_first_inorder(tree), expected_inorder)

    def test_depth_first_postorder(self):
        self.assertEqual(Tree().depth_first_postorder(), [])
        tree = Tree(1)
        root = Tree_root(tree)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        child3 = TreeNode(4)
        root.add_child(child1)
        root.add_child(child2)
        child2.add_child(child3)

        expected_postorder = [child1, child3, child2, root]
        self.assertEqual(Tree_depth_first_postorder(tree), expected_postorder)


if __name__ == '__main__':
    unittest.main()
