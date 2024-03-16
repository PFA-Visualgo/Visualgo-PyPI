""":demand: F1.8"""

import unittest
from visualgo.structures.Table import *


class TestTable(unittest.TestCase):
    """
    This class tests the Table class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a table.
        """
        self.assertRaises(TypeError, lambda: Table())
        table2 = Table(3)
        self.assertRaises(TypeError, lambda: Table(None))

    def test_length(self):
        """
        Tests the `length` method.
        """
        table = Table(5)
        self.assertEqual(table.length, 5)
        table2 = Table(0)
        self.assertEqual(Table_length(table2), 0)

    def test_get(self):
        """
        Tests the `get` method.
        """
        table = Table(4)
        for i in range(4):
            table.set(i, 2 * i)
        for i in range(3):
            self.assertEqual(table.get(i), 2 * i)
        self.assertEqual(Table_get(table, 3), 6)

    def test_set(self):
        """
        Tests the `set` method.
        """
        table = Table(4)
        for i in range(4):
            table.set(i, 2 * i)
        for i in range(4):
            table.set(i, 3 * i)
        for i in range(4):
            self.assertEqual(table.get(i), 3 * i)
        self.assertRaises(IndexError, lambda: Table_set(table, 4, 89))



if __name__ == '__main__':
    unittest.main()
