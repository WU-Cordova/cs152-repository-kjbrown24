# datastructures.array.Array

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

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence must be a valid sequence type.")
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid type.")
        if not isinstance (starting_sequence[0], data_type):
            raise TypeError("Need to pass in same data types")
        self.__elements = np.array(starting_sequence, dtype= data_type)
        self.__logical = len(starting_sequence)
        self.__physical = len(self.__elements)
        self.__data_type = data_type if data_type != object else type(starting_sequence[0])

    #def __getitem__(self, index: slice) -> Sequence[T]:
     #   item = self.__elements[index]
      #  return item.item() if isinstance(item, np.generic) else item

    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            if  not isinstance(index, slice) and not isinstance(index, int):
                raise TypeError("Needs to be int or slice")
            if isinstance(index, slice):

                start, stop = index.start, index.stop

                if start is None:
                    start = 0
                if stop is None:
                    stop = self.__logical - 1
                
                if start >= self.__logical or stop > self.__logical:
                    raise IndexError('Not in Bounds')
                
                items = []
                for item in range(len(self.__elements)):
                    items.append(item if not isinstance(item, np.generic) else item.item())
                
                items_to_return = self.__elements[index].tolist()
                return Array(starting_sequence= items_to_return, data_type = self.__data_type)
                
            return self.__elements[index] if not isinstance(self.__elements[index], np.generic) else self.__elements[index].item()
    
    
    def __setitem__(self, index: int, item: T) -> None:
        if type(item) != self.__data_type:
            raise TypeError("Item you're setting isn't same type as array")
        if index > self.__logical:
            raise IndexError("Index out of bounds")
        self.__elements[index] = item

    def append(self, data: T) -> None:
        if type(data) != self.__data_type:
            raise ValueError("Data is the wrong type")
        if self.__logical == self.__physical:
            self.__physical *= 2
            self.__elements.resize(self.__physical)
        
        self.__logical += 1
        self.__elements[self.__logical] = data

    def append_front(self, data: T) -> None:
        if type(data) != self.__data_type:
            raise ValueError("Data is the wrong type")
        if self.__logical == self.__physical:
            self.__physical *= 2
            self.__elements.resize(self.__physical)
        for i in range(self.__logical -1, 0, -1):
            self.__elements[i +1] = self.__elements[i]
        self.__elements[0] = data
        self.__logical += 1

    def pop(self) -> None:
        del self[self.__logical-1]
    
    def pop_front(self) -> None:
        del self[self.__logical[0]]

    def __len__(self) -> int: 
        return self.__logical

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Array):
            if self.__data_type == other.__data_type and (self.__elements == other.__elements).all() and self.__logical == other.__logical and self.__physical == other.__physical:
                return True
        return False
    
    def __ne__(self, other):
        return not self==other

    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements[:self.__logical])

    def __reversed__(self) -> Iterator[T]:
        reversed_elements = self.__elements[self.__logical-1::-1]
        return iter(reversed_elements)

    """ def __resize__(self, new_size):
        if new_size < 0:
            raise ValueError("New size isn't possible. Need a positive int")
        if self.__physical > new_size:
            default = self.__data_type
            new_items = default * new_size - len(self.__elements)
            np.append( self.__elements, new_items)
            self.__physical = new_size
        else:
            self.__elements = self.__elements[0:new_size]
            if self.__logical > new_size:
                self.__logical = new_size"""

    def __delitem__(self, index: int) -> None:
        for i in range(index, self.__logical -1):
            self.__elements[i] = self.__elements[i + 1]
        self.__logical -= 1
        if self.__logical <= self.__physical/4:
            self.__physical/=2
            self.__elements.resize(self.__physical)


    def __contains__(self, item: Any) -> bool:
        return item in self.__elements[:self.__logical]

    def clear(self) -> None:
        self.__elements = np.array([])
        self.__logical = 0
        self.__physical = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical}, Physical: {self.__physical}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')