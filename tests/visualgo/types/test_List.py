""":demand: F1.8"""

import unittest
from visualgo.types import List


class TestList(unittest.TestCase):
    """
    This class tests the List class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a list.
        """
        lis = List()
        self.assertEqual(lis.length(), 0)
        lis2 = List([1, 2, 89])
        self.assertEqual(lis2.length(), 3)

    def test_length(self):
        """
        Tests the `length` method.
        """
        lis = List()
        self.assertEqual(lis.length(), 0)
        lis2 = List([1, 2, 89])
        self.assertEqual(lis2.length(), 3)
        lis3 = List([1, 2])
        self.assertEqual(lis3.length(), 2)

    def test_get(self):
        """
        Tests the `get` method.
        """
        lis = List([1, 2, 89])
        self.assertEqual(lis.get(0), 1)
        self.assertEqual(lis.get(2), 89)
        self.assertEqual(lis.get(1), 2)
        self.assertRaises(IndexError, lambda: lis.get(4))

    def test_insert(self):
        """
        Tests the `insert` method.
        """
        lis = List([1, 2, 89])
        lis.insert(1, 6)
        self.assertEqual(lis.get(1), 6)
        self.assertRaises(IndexError, lambda: lis.insert(4, "e"))

    def test_delete(self):
        """
        Tests the `delete` method.
        """
        lis = List([1, 2, 89])
        lis.delete(1)
        self.assertEqual(lis.get(1), 89)
        self.assertRaises(IndexError, lambda: lis.delete(2))


if __name__ == '__main__':
    unittest.main()
