"""
Project 8 - Heaps - Solution Code
CSE 331 Fall 2022
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
        Determines the length of the min heap

        :return: an int representing the size of the heap
        """
        if self.data is not None:
            return len(self.data)

    def empty(self) -> bool:
        """
        Determines if the min heap is empty

        :return:a boolean true if the min heap has no elements, False otherwise
        """
        if len(self.data) == 0:
            return True

        return False

    def top(self) -> T:
        """
        Finds the top or min value of the min heap

        :return: an object, the minimum value of the min heap
        """
        if not self.empty():
            return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
        Retrieves the index of the left child based on the given index

        :param index: the index of the parent node
        :return: an int representing the index of the left child
        """
        if 2 * index + 1 < len(self.data):
            return 2 * index + 1

    def get_right_child_index(self, index: int) -> int:
        """
        Retrieves the index of the right child based on the given index

        :param index: the index of the parent node
        :return: an int representing the index of the right child
        """
        if 2 * index + 2 < len(self.data):
            return 2 * index + 2

    def get_parent_index(self, index: int) -> int:
        """
        Retrieves the index of the parents node based on the given index

        :param index: the index of the parent node
        :return: an int representing the index of the parent child
        """
        if (index - 1) // 2 >= 0:
            return (index - 1) // 2

    def get_min_child_index(self, index: int) -> int:
        """
        Computes the index of the child with the lower value

        :param index: the index of the parent
        :return: an int w/ the min value child's index, None if no children
        """
        if not self.empty():
            lc = self.get_left_child_index(index)
            rc = self.get_right_child_index(index)

            if lc is None and rc is None:  # no children
                return None

            if lc is not None and rc is not None:  # both children
                if self.data[lc] < self.data[rc]:
                    return lc
                elif self.data[lc] >= self.data[rc]:
                    return rc

            if lc is not None and rc is None:  # only left child
                return lc

    def percolate_up(self, index: int) -> None:
        """
        Percolates up the value at index to its valid spot in the heap

        :param index: the index of the node to be percolated
        :return: None
        """
        if index > 0:
            par = self.get_parent_index(index)
            if self.data[index] <= self.data[par]:
                self.data[index], self.data[par] = self.data[par], self.data[index]
                self.percolate_up(par)

    def percolate_down(self, index: int) -> None:
        """
        Percolates down the value at index to its valid spot in the heap

        :param index: the index of the node to be percolated
        :return: None
        """
        lc = self.get_left_child_index(index)
        rc = self.get_right_child_index(index)
        if lc is not None:
            small = lc
            if rc is not None:
                if self.data[rc] < self.data[lc]:
                    small = rc
            if self.data[index] >= self.data[small]:
                self.data[index], self.data[small] = self.data[small], self.data[index]
                self.percolate_down(small)

    def push(self, val: T) -> None:
        """
        Pushed the value to the heap and moves to proper position

        :param val: the object to be added to the min heap
        :return: None
        """
        end = len(self.data)
        self.data.append(val)
        self.percolate_up(end)

    def pop(self) -> T:
        """
        Removes the top el from the heap, restores items to valid position

        :return: The value that was popped
        """
        if not self.empty():
            val = self.data[0]
            if min is not None:
                self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
                self.data.remove(val)
                self.percolate_down(0)
                return val
            self.data.remove(val)
            return val


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
        Checks to see if heap is empty

        :return: A boolean True if heap is empty, False otherwise
        """
        return self.data.data.empty()

    def top(self) -> int:
        """
        Gets the max value of the heap

        :return: The top value of the heap
        """
        if not self.data.empty():
            return -1 * self.data.data[0]

    def push(self, key: int) -> None:
        """
        Pushed the value to the heap

        :param key: the value to be added to the heap
        :return: None
        """
        return self.data.push(-1 * key)

    def pop(self) -> int:
        """
        Removes the top element from the heap

        :return: The value that was popped
        """
        return -1 * self.data.pop()


def get_eating_times(values: List[List[List[int]]]) -> List[List[int]]:
    """
    Takes in a list of interval lists such that each sublist returns a list of
    finite-length intervals that do not overlap with any of the given intervals

    :param values: List of interval lists
    :return: a list of non overlapping intervals
    """
    sol = []
    if len(values) > 0:
        min_heap = MinHeap()
        for memb in values:
            for sub in memb:
                min_heap.push(sub)

        stack = []
        stack.append(min_heap.pop())
        while not min_heap.empty():
            val = min_heap.pop()
            if stack[-1][0] <= val[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], val[-1])
            else:
                stack.append(val)

        i = 0
        while i < len(stack) - 1:
            if stack[i][1] < stack[i + 1][0]:
                sol.append([stack[i][1], stack[i + 1][0]])
            i += 1

    return sol
