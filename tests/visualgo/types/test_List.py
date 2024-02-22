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


if __name__ == '__main__':
    unittest.main()
