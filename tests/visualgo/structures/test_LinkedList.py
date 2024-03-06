""":demand: F1.8"""

import unittest
from visualgo.structures import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    This class tests the LinkedList class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a linked list.
        """
        lis = LinkedList()
        self.assertEqual(lis.length, 0)
        self.assertTrue(hasattr(lis, 'head'))
        self.assertTrue(hasattr(lis, 'length'))

    def test_length(self):
        """
        Tests the `length` method.
        """
        lis = LinkedList()
        self.assertEqual(lis.length, 0)
        lis.insert_head(1)
        self.assertEqual(lis.length, 1)
        lis.insert_head(2)
        self.assertEqual(lis.length, 2)
        lis.delete(1)
        self.assertEqual(lis.length, 1)

    def test_get(self):
        """
        Tests the `get` method.
        """
        lis = LinkedList()
        lis.insert_head(1)
        self.assertEqual(lis.get(0), 1)
        lis.insert_head(2)
        self.assertEqual(lis.get(0), 2)
        self.assertEqual(lis.get(1), 1)
        self.assertRaises(IndexError, lambda: lis.get(3))

    def test_head(self):
        """
        Tests the `insert_head` and `get_head` methods.
        """
        lis = LinkedList()
        lis.insert_head(1)
        self.assertEqual(lis.head, 1)
        lis.insert_head(2)
        self.assertEqual(lis.head, 2)
        self.assertEqual(lis.get(1), 1)

    def test_delete(self):
        """
        Tests the `delete` method.
        """
        lis = LinkedList()
        lis.insert_head(1)
        lis.delete(0)
        self.assertEqual(lis.length, 0)
        lis.insert_head(1)
        lis.insert_head(2)
        lis.delete(0)
        self.assertEqual(lis.get(0), 1)

    def test_is_empty(self):
        """
        Tests the `is_empty` method.
        """
        lis = LinkedList()
        self.assertTrue(lis.is_empty())
        lis.insert_head(1)
        self.assertFalse(lis.is_empty())

    def test_insert_after(self):
        """
        Tests the `insert_after` method.
        """
        lis = LinkedList()
        lis.insert_head(1)
        lis.insert_after(0, 2)
        self.assertEqual(lis.get(1), 2)
        lis.insert_after(0, 3)
        self.assertEqual(lis.get(1), 3)
        self.assertEqual(lis.get(2), 2)
        self.assertRaises(IndexError, lambda: lis.insert_after(3, 4))


if __name__ == '__main__':
    unittest.main()
