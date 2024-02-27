""":demand: F1.8"""

import unittest
from visualgo.types import Set, List, LinkedList


class TestSet(unittest.TestCase):
    """
    This class tests the Set class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a set.
        """
        set = Set()
        set2 = Set([8, 7])
        set3 = Set(List([1, 2, 3]))
        set4 = Set(LinkedList([100, 62, 43]))

    def test_is_empty(self):
        """
        Tests the `is_empty` method.
        """
        set = Set()
        self.assertTrue(set.is_empty())
        set2 = Set([6])
        self.assertFalse(set2.is_empty())

    def test_is_in(self):
        """
        Tests the `is_in` method.
        """
        set = Set([0, 1, 2, 3, 5, 6, 7])
        for i in range(4):
            self.assertTrue(set.is_in(i))
        for i in range(4, 7):
            self.assertTrue(set.is_in(i + 1))
        self.assertFalse(set.is_in(-1))
        self.assertFalse(set.is_in(4))
        self.assertFalse(set.is_in(8))

    def test_add(self):
        """
        Tests the `add` method.
        """
        set = Set()
        self.assertFalse(set.is_in(6))
        set.add(6)
        self.assertTrue(set.is_in(6))
        set.add(6)
        set.delete(6)
        self.assertFalse(set.is_in(6))
        self.assertFalse(set.is_in(None))
        set.add(None)
        self.assertTrue(set.is_in(None))

    def test_delete(self):
        """
        Tests the `delete` method.
        """
        set = Set()
        set.add(57)
        set.delete(57)
        self.assertFalse(set.is_in(57))
        self.assertRaises(KeyError, lambda: set.delete(57))


if __name__ == '__main__':
    unittest.main()
