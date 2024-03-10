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
        print(lis, lis2)

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
        lis = DoublyLinkedList([1, 2, 89])
        self.assertEqual(lis._get_node(0).next, lis._get_node(1))
        self.assertEqual(lis._get_node(1).next, lis._get_node(2))
        self.assertRaises(IndexError, lambda: lis._get_node(3))

    def test_set(self):
        """
        Tests the `set` method.
        """
        lis = DoublyLinkedList([1, 2, 89])
        lis.set(0, "Interruption.")
        lis.set(1, [78])
        lis.set(2, None)
        self.assertEqual(lis.get(0), "Interruption.")
        self.assertEqual(lis.get(1), [78])
        self.assertIsNone(lis.get(2))

    def test_insert_head(self):
        """
        Tests the `insert_head` method.
        """
        lis = DoublyLinkedList()
        lis.insert_head(90)
        self.assertEqual(lis.get(0), 90)
        lis.insert_head(-3)
        self.assertEqual(lis.get(0), -3)
        self.assertEqual(lis.get(1), 90)

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
        lis.insert_before(0, 33)
        self.assertEqual(lis.get(0), 33)
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
        lis.delete(0)
        self.assertEqual(lis.get(0), 89)


if __name__ == '__main__':
    unittest.main()
