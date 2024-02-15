from typing import TypeVar

T = TypeVar('T')


class Queue:
    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.
        :return: bool
        """
        pass

    def enqueue(self, e: T) -> None:
        """
        Adds an element to the end of the queue.
        :param e: Object
        :return: None
        """
        pass

    def dequeue(self) -> T:
        """
        Removes an element from the head of the queue and returns it.
        :return: Object
        """
        pass

    def head(self) -> T:
        """
        Returns the head of the queue.
        :return:
        """
        pass
