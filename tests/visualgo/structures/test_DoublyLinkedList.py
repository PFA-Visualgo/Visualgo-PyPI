""":demand: F1.8"""

import unittest
from visualgo.structures import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    """
    This class tests the DoublyLinkedList class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a linked list.
        Same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList()
        self.assertEqual(lis.length, 0)
        lis2 = DoublyLinkedList([1, 2, 89])
        self.assertEqual(lis2.length, 3)

    def test_head(self):
        """
        Tests the `insert_head` and `get_head` methods.
        Not the same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList([1, 2, 89])
        self.assertEqual(lis.head, 1)
        lis.insert_head(5)
        self.assertEqual(lis.head, 5)

    def test_length(self):
        """
        Tests the `length` method.
        Same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList()
        self.assertEqual(lis.length, 0)
        lis2 = DoublyLinkedList([1, 2, 89])
        self.assertEqual(lis2.length, 3)
        lis3 = DoublyLinkedList([1, 2])
        self.assertEqual(lis3.length, 2)

    def test_is_empty(self):
        """
        Tests the `is_empty` method.
        Same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList()
        self.assertTrue(lis.is_empty())
        lis.insert_head(1)
        self.assertFalse(lis.is_empty())
        lis2 = DoublyLinkedList([1, 2, 89])
        self.assertFalse(lis2.is_empty())

    def test_get(self):
        """
        Tests the `get` method.
        Not the same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList([1, 2, 89])
        self.assertEqual(lis.get(0), 1)
        self.assertEqual(lis.get(1), 2)
        self.assertEqual(lis.get(2), 89)

        self.assertRaises(IndexError, lambda: lis.get(4))

    def test_get_node(self):
        """
        Tests the `get_node` method.
        """
        pass

    def test_set(self):
        """
        Tests the `set` method.
        """
        pass

    def test_insert_head(self):
        """
        Tests the `insert_head` method.
        """
        pass

    def test_insert_after(self):
        """
        Tests the `insert_after` method.
        Same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList([1, 2, 89])
        lis.insert_after(0, 3)
        self.assertEqual(lis.get(1), 3)
        lis.insert_after(3, 33)
        self.assertEqual(lis.get(4), 33)
        self.assertRaises(IndexError, lambda: lis.insert_after(5, 0))

    def test_insert_last(self):
        """
        Tests the `insert_last` method.
        """
        lis = DoublyLinkedList()
        lis.insert_last(1)
        self.assertEqual(lis.get(0), 1)

        lis2 = DoublyLinkedList([1, 2, 89])
        lis2.insert_last(-5)
        self.assertEqual(lis2.get(3), -5)

    def test_insert_before(self):
        """
        Tests the `insert_after` method.
        """
        lis = DoublyLinkedList([1, 2, 89])
        lis.insert_before(1, 3)
        self.assertEqual(lis.get(1), 3)
        lis.insert_before(4, 33)
        self.assertEqual(lis.get(4), 33)
        self.assertRaises(IndexError, lambda: lis.insert_before(-1, 0))

    def test_delete(self):
        """
        Tests the `delete` method.
        Not the same as in `test_LinkedList`.
        """
        lis = DoublyLinkedList([1, 2, 89])
        lis.delete(1)
        self.assertEqual(lis.get(1), 89)
        self.assertRaises(IndexError, lambda: lis.delete(2))


if __name__ == '__main__':
    unittest.main()
