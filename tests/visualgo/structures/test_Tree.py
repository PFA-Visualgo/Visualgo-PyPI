import unittest
from visualgo.structures.Tree import Tree, TreeNode

class TestTree(unittest.TestCase):
    def test_depth_first_preorder(self):
        tree = Tree(1)
        root = tree.root
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        child3 = TreeNode(4)
        root.add_child(child1)
        root.add_child(child2)
        child2.add_child(child3)

        expected_preorder = [root, child1, child2, child3]
        self.assertEqual(tree.depth_first_preorder(), expected_preorder)

    def test_depth_first_inorder(self):
        tree = Tree(2)
        root = tree.root
        child1 = TreeNode(1)
        child2 = TreeNode(3)
        child3 = TreeNode(4)
        root.add_child(child1)
        root.add_child(child2)
        child2.add_child(child3)

        expected_inorder = [child1, child3, child2, root]
        self.assertEqual(tree.depth_first_inorder(), expected_inorder)

    def test_depth_first_postorder(self):
        tree = Tree(1)
        root = tree.root
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        child3 = TreeNode(4)
        root.add_child(child1)
        root.add_child(child2)
        child2.add_child(child3)

        expected_postorder = [child1, child3, child2, root]
        self.assertEqual(tree.depth_first_postorder(), expected_postorder)

if __name__ == '__main__':
    unittest.main()
