""":demand: F1.8"""

import unittest
from visualgo.structures.LinkedList import *


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
        self.assertIsNone(lis.head)
        self.assertEqual(lis.length, 0)
        lis2 = LinkedList([9, 0, 7])
        self.assertEqual(lis2[0], 9)
        self.assertEqual(lis2[1], 0)
        self.assertEqual(lis2[2], 7)
        self.assertEqual(lis2.length, 3)
        print(lis, lis2)

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
        self.assertEqual(LinkedList_length(lis), 1)

    def test_is_empty(self):
        """
        Tests the `is_empty` method.
        """
        lis = LinkedList()
        self.assertTrue(lis.is_empty())
        lis.insert_head(1)
        self.assertFalse(LinkedList_is_empty(lis))

    def test_get(self):
        """
        Tests the `get` method.
        """
        lis = LinkedList()
        lis.insert_head(1)
        self.assertEqual(lis.get(0), 1)
        lis.insert_head(2)
        self.assertEqual(lis.get(0), 2)
        self.assertEqual(LinkedList_get(lis, 1), 1)
        self.assertRaises(IndexError, lambda: lis.get(3))

    def test_get_node(self):
        """
        Tests the `get_node` method.
        """
        lis = LinkedList([1, 2, 89])
        self.assertEqual(lis._get_node(0).next, lis._get_node(1))
        self.assertEqual(LinkedList__get_node(lis, 1).next, lis._get_node(2))
        self.assertRaises(IndexError, lambda: lis._get_node(3))

    def test_set(self):
        """
        Tests the `set` method.
        """
        lis = LinkedList([1, 2, 89])
        lis.set(0, "Et ouais.")
        lis.set(1, [78])
        LinkedList_set(lis, 2, None)
        self.assertEqual(lis.get(0), "Et ouais.")
        self.assertEqual(lis.get(1), [78])
        self.assertIsNone(lis.get(2))
        self.assertRaises(IndexError, lambda: lis._get_node(3))

    def test_insert_head(self):
        """
        Tests the `insert_head` and `get_head` methods.
        """
        lis = LinkedList()
        lis.insert_head(1)
        self.assertEqual(lis.head, 1)
        LinkedList_insert_head(lis, 2)
        self.assertEqual(lis.head, 2)
        self.assertEqual(lis.get(1), 1)

    def test_insert_after(self):
        """
        Tests the `insert_after` method.
        """
        lis = LinkedList()
        lis.insert_head(1)
        lis.insert_after(0, 2)
        self.assertEqual(lis.get(1), 2)
        LinkedList_insert_after(lis, 0, 3)
        self.assertEqual(lis.get(1), 3)
        self.assertEqual(lis.get(2), 2)
        self.assertRaises(IndexError, lambda: lis.insert_after(3, 4))

    def test_insert(self):
        """
        Tests the `insert` method.
        """
        lis = LinkedList()
        lis.insert_head(1)
        lis.insert(0, 2)
        self.assertEqual(lis.get(0), 2)
        LinkedList_insert(lis, 1, 3)
        self.assertEqual(lis.get(1), 3)
        self.assertEqual(lis.get(0), 2)
        self.assertRaises(IndexError, lambda: lis.insert(-1, 4))

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
        LinkedList_delete(lis, 0)
        self.assertEqual(lis.get(0), 1)
        self.assertRaises(IndexError, lambda: lis.delete(1))


if __name__ == '__main__':
    unittest.main()
