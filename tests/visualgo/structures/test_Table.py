""":demand: F1.8"""

import unittest
from visualgo.structures import Table


class TestTable(unittest.TestCase):
    """
    This class tests the Table class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a table.
        """
        self.assertRaises(SyntaxError, lambda: Table())
        table2 = Table(3)
        self.assertRaises(TypeError, lambda: Table(None))

    def test_get(self):
        """
        Tests the `get` method.
        """
        table = Table(4)
        for i in range(4):
            table.set(i, 2 * i)
        for i in range(4):
            self.assertEqual(table.get(i), 2 * i)

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
        self.assertRaises(IndexError, lambda: table.set(4, 89))

    def test_length(self):
        """
        Tests the `length` method.
        """
        table = Table(5)
        self.assertEqual(table.length(), 5)
        table2 = Table(0)
        self.assertEqual(table2.length(), 0)


if __name__ == '__main__':
    unittest.main()
