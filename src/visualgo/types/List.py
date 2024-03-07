from typing import TypeVar

T = TypeVar('T')


class List:
    def length(self) -> int:
        """
        Returns the length of the list.
        :return: int
        """
        pass

    def get(self, index: int) -> T:
        """
        Returns the element at the `index` position.
        :param index: int
        :return: Object
        """
        pass

    def insert_after(self, index: int,
                     e: T) -> None:  # TODO : Changer nom de la méthode dans le diagramme des classes et cahier des charges
        """
        Inserts the element after the given `index`.
        :param index: int
        :param e: Object
        :return: None
        """
        pass

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given `index`.
        :param index: int
        :return: None
        """
        pass
