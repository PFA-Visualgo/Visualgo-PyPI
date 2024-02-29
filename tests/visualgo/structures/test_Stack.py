""":demand: F1.8"""

import unittest
from visualgo.structures import Stack


class AugmentedStack(Stack):
    """
    This class adds the possibility to get the actual node at the top instead of the value.
    This helps to test more accurately.
    """
    def __init__(self):
        super().__init__()

    def top_node(self):
        return self._top


class TestStack(unittest.TestCase):
    """
    This class tests the Stack class.
    The `top` method is tested throughout these tests.
    """

    def test_creation(self):
        """
        Tests the instantiation of a stack.
        """
        stack = AugmentedStack()
        self.assertTrue(stack.top_node().is_sentinel())

    def test_push(self):
        """
        Tests the push method.
        """
        stack = AugmentedStack()
        stack.push(1)
        self.assertEqual(stack.top().content(), 1)
        self.assertFalse(stack.top_node().is_sentinel())

    def test_pop(self):
        """
        Tests the pop method.
        """
        stack = AugmentedStack()
        stack.push(34)
        self.assertEqual(stack.pop(), 34)
        self.assertTrue(stack.top_node().is_sentinel())
        stack.push([90])
        stack.push(None)
        self.assertFalse(stack.top_node().is_sentinel())
        self.assertEqual(stack.pop(), None)
        self.assertFalse(stack.top_node().is_sentinel())
        self.assertEqual(stack.pop(), [90])
        self.assertTrue(stack.top_node().is_sentinel())

    def test_is_empty(self):
        """
        Tests the is_empty method.
        """
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push("j")
        self.assertFalse(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
