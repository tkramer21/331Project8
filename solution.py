"""
Project 8 - Heaps - Solution Code
CSE 331 Fall2022
Onsay
"""

from typing import TypeVar, List

T = TypeVar('T')


class MinHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def empty(self) -> bool:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def top(self) -> T:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def get_left_child_index(self, index: int) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def get_right_child_index(self, index: int) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def get_parent_index(self, index: int) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def get_min_child_index(self, index: int) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def percolate_up(self, index: int) -> None:
        """
        INSERT DOCSTRING HERE
        """
        pass
    def percolate_down(self, index: int) -> None:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def push(self, val: T) -> None:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def pop(self) -> T:
        """
        INSERT DOCSTRING HERE
        """
        pass


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    __repr__ = __str__

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def top(self) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def push(self, key: int) -> None:
        """
        INSERT DOCSTRING HERE
        """
        pass

    def pop(self) -> int:
        """
        INSERT DOCSTRING HERE
        """
        pass


def get_eating_times(values: List[List[List[int]]]) -> List[List[int]]:
    """
    INSERT DOCSTRING HERE
    """
    pass
