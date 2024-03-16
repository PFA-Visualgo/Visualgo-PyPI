""":demand: F1.8"""

import unittest
from visualgo.structures.StackLL import *


class AugmentedStack(Stack):
    """
    This class adds the possibility to get the actual node at the top instead of the value.
    This helps to test more accurately.
    """

    def __init__(self):
        super().__init__()

    def top_node(self):
        return self.top


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
        self.assertTrue(stack.is_empty())
        stack2 = AugmentedStack()
        for i in range(4):
            stack2.push(i)
        Stack_push(stack2, 4)
        print(stack, stack2)

    def test_push(self):
        """
        Tests the push method.
        """
        stack = AugmentedStack()
        stack.push(1)
        self.assertEqual(stack.top, 1)
        self.assertFalse(stack.is_empty())
        Stack_push(stack, 2)
        self.assertEqual(Stack_top(stack), 2)

    def test_pop(self):
        """
        Tests the pop method.
        """
        stack = AugmentedStack()
        stack.push(34)
        self.assertEqual(stack.pop(), 34)
        self.assertTrue(stack.is_empty())
        stack.push([90])
        stack.push(None)
        self.assertFalse(stack.is_empty())
        self.assertIsNone(stack.pop())
        self.assertFalse(stack.is_empty())
        self.assertEqual(Stack_pop(stack), [90])
        self.assertTrue(stack.is_empty())
        self.assertRaises(IndexError, lambda: stack.pop())

    def test_is_empty(self):
        """
        Tests the is_empty method.
        """
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push("j")
        self.assertFalse(Stack_is_empty(stack))


if __name__ == '__main__':
    unittest.main()
