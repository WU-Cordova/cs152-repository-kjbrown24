# datastructures.array.Array
#complete 1

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray

from datastructures.iarray import IArray, T

class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T] = [], data_type: type = object) -> None: 
        """
        Initializes the Array with an optional starting sequence and data type.
        Ensures type consistency and pre-allocates memory for efficiency.
        """
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence must be a valid sequence type.")
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid type.")
        if starting_sequence and data_type != type(starting_sequence[0]):
            raise TypeError("All elements must be of the same data type.")
        
        self.__data_type = data_type if data_type != object and starting_sequence else object
        self.__elements = np.array(starting_sequence, dtype=self.__data_type)
        self.__logical = len(starting_sequence)  # Number of elements in use
        self.__physical = max(2 * self.__logical, 1)  # Allocated memory size
        self.__elements.resize(self.__physical)

    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        """
        Retrieves an element or a slice of elements from the array.
        """
        if not isinstance(index, (int, slice)):
            raise TypeError("Index must be an int or a slice.")
        if isinstance(index, int) and (index < 0 or index >= self.__logical):
            raise IndexError("Index out of bounds.")
        return self.__elements[:self.__logical][index]
    
    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the value of an element at a given index.
        """
        if not isinstance(item, self.__data_type):
            raise TypeError("Item must match the array data type.")
        if index < 0 or index >= self.__logical:
            raise IndexError("Index out of bounds.")
        self.__elements[index] = item

    def append(self, data: T) -> None:
        """
        Adds an element to the end of the array, resizing if necessary.
        """
        if not isinstance(data, self.__data_type):
            raise TypeError("Data must match the array data type.")
        if self.__logical == self.__physical:
            self.__physical *= 2  # Double the capacity when needed
            self.__elements.resize(self.__physical)
        self.__elements[self.__logical] = data
        self.__logical += 1

    def append_front(self, data: T) -> None:
        """
        Adds an element to the front of the array, shifting elements as needed.
        """
        if not isinstance(data, self.__data_type):
            raise TypeError("Data must match the array data type.")
        if self.__logical == self.__physical:
            self.__physical *= 2
            self.__elements.resize(self.__physical)
        self.__elements[1:self.__logical+1] = self.__elements[:self.__logical]
        self.__elements[0] = data
        self.__logical += 1

    def pop(self) -> None:
        """
        Removes the last element, reducing capacity if necessary.
        """
        if self.__logical == 0:
            raise IndexError("Cannot pop from an empty array.")
        self.__logical -= 1
        if self.__logical <= self.__physical // 4:
            self.__physical //= 2
            self.__elements.resize(self.__physical)
    
    def pop_front(self) -> None:
        """
        Removes the first element, shifting elements left.
        """
        if self.__logical == 0:
            raise IndexError("Cannot pop from an empty array.")
        self.__elements[:self.__logical-1] = self.__elements[1:self.__logical]
        self.__logical -= 1
        if self.__logical <= self.__physical // 4:
            self.__physical //= 2
            self.__elements.resize(self.__physical)

    def __len__(self) -> int: 
        """Returns the logical size of the array."""
        return self.__logical

    def __eq__(self, other: object) -> bool:
        """
        Compares two arrays for equality based on type, elements, and capacity.
        """
        if isinstance(other, Array):
            return (
                self.__data_type == other.__data_type and
                np.array_equal(self.__elements[:self.__logical], other.__elements[:other.__logical]) and
                self.__logical == other.__logical and
                self.__physical == other.__physical
            )
        return False
    
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the array's elements."""
        return iter(self.__elements[:self.__logical])

    def __reversed__(self) -> Iterator[T]:
        """Returns a reversed iterator over the array's elements."""
        return iter(self.__elements[self.__logical-1::-1])

    def __delitem__(self, index: int) -> None:
        """
        Deletes an element at the given index and shifts elements left.
        """
        if index < 0 or index >= self.__logical:
            raise IndexError("Index out of bounds.")
        self.__elements[index:self.__logical-1] = self.__elements[index+1:self.__logical]
        self.__logical -= 1
        if self.__logical <= self.__physical // 4:
            self.__physical //= 2
            self.__elements.resize(self.__physical)

    def __contains__(self, item: Any) -> bool:
        """Checks if an item exists in the array."""
        return item in self.__elements[:self.__logical]

    def clear(self) -> None:
        """Clears the array, resetting its size and capacity."""
        self.__elements = np.empty(1, dtype=self.__data_type)
        self.__logical = 0
        self.__physical = 1

    def __str__(self) -> str:
        """Returns a string representation of the array."""
        return '[' + ', '.join(str(item) for item in self.__elements[:self.__logical]) + ']'
    
    def __repr__(self) -> str:
        """Returns a detailed string representation of the array."""
        return f'Array {self.__str__()}, Logical: {self.__logical}, Physical: {self.__physical}, type: {self.__data_type}'
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
