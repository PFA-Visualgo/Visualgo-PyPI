""":demand: F1.8"""

import unittest
from visualgo.structures import Queue


class TestQueue(unittest.TestCase):
    """
    This class tests the Queue class.
    """

    def test_creation(self):
        """
        Tests the instantiation of a queue.
        """
        queue = Queue()
        # Also tests the possibility to initiliaze a queue with a list ?

    def test_is_empty(self):
        """
        Tests the `is_empty` method.
        """
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(5)
        self.assertFalse(queue.is_empty())

    def test_enqueue_dequeue(self):
        """
        Tests the `enqueue` and `dequeue` methods.
        """
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)
        self.assertTrue(queue.is_empty())
        queue.enqueue(9)
        queue.enqueue(17)
        self.assertEqual(queue.dequeue(), 9)
        self.assertEqual(queue.dequeue(), 17)
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
