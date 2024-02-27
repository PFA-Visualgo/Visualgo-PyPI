""":demand: F1.8"""

import unittest
from visualgo.types import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    This class tests the List class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a linked list.
        """
        lis = LinkedList()
        self.assertEqual(lis.length(), 0)
        lis2 = LinkedList([1, 2, 89])
        self.assertEqual(lis2.length(), 3)

    def test_length(self):
        """
        Tests the `length` method.
        """
        lis = LinkedList()
        self.assertEqual(lis.length(), 0)
        lis2 = LinkedList([1, 2, 89])
        self.assertEqual(lis2.length(), 3)
        lis3 = LinkedList([1, 2])
        self.assertEqual(lis3.length(), 2)

    def test_get(self):
        """
        Tests the `get` method.
        """
        lis = LinkedList([1, 2, 89])
        self.assertEqual(lis.get(0), 1)
        self.assertEqual(lis.get(2), 89)
        self.assertEqual(lis.get(1), 2)
        self.assertRaises(IndexError, lambda: lis.get(4))

    def test_head(self):
        """
        Tests the `insert_head` and `get_head` methods.
        """
        lis = LinkedList([1, 2, 89])
        self.assertEqual(lis.get_head(), 1)
        lis.insert_head(5)
        self.assertEqual(lis.get_head(), 5)

    def test_delete(self):
        """
        Tests the `delete` method.
        """
        lis = LinkedList([1, 2, 89])
        lis.delete(1)
        self.assertEqual(lis.get(1), 89)
        self.assertRaises(IndexError, lambda: lis.delete(2))

    def test_is_empty(self):
        """
        Tests the `is_empty` method.
        """
        lis = LinkedList()
        self.assertTrue(lis.is_empty())
        lis.insert_head(1)
        self.assertFalse(lis.is_empty())
        lis2 = LinkedList([1, 2, 89])
        self.assertFalse(lis2.is_empty())

    def test_insert_after(self):
        """
        Tests the `insert_after` method.
        """
        lis = LinkedList([1, 2, 89])
        lis.insert_after(0, 3)
        self.assertEqual(lis.get(1), 3)
        lis.insert_after(3, 33)
        self.assertEqual(lis.get(4), 33)
        self.assertRaises(IndexError, lambda: lis.insert_after(5, 0))


if __name__ == '__main__':
    unittest.main()
