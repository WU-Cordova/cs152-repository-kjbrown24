from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def __getitem__(self, column_index: int) -> T:
            if column_index >= self.num_columns:
                raise IndexError("Index too big.")
            index = self.map_index(self.row_index, column_index)

            return self.array[index]
        
        
        def map_index(self, row_index, column_index):
            return row_index * self.num_columns + column_index
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index= column_index)

            self.array[index] = value
            
        
        def __iter__(self) -> Iterator[T]:
            
            for column_index in range(self.num_columns):
                yield self[column_index]
                
        
        def __reversed__(self) -> Iterator[T]:
            for col_num in reversed(range(self.num_columns)):
                yield self[col_num]
            raise NotImplementedError('Row.__reversed__ not implemented.')

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:

        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Entered sequence is not a sequence.")
        
        for element in starting_sequence:
            if not isinstance(element, Sequence):
                raise ValueError("")
            
            for item in element:
                if not isinstance(item, data_type):
                    raise ValueError("All items must be of the same type")

        self.data_type = data_type
        self.row_len = len(starting_sequence)
        self.column_len = len(starting_sequence[0])

        for element in starting_sequence:
            if self.column_len != len(element):
                raise ValueError("Your sequences are not all equally long.")
        
        self.array2D = Array([data_type() for item in range(self.row_len * self.column_len)], data_type= data_type)

        index = 0
        for row_index in range(self.row_len):
            for column_index in range(self.column_len):
                
                self.array2D[index] = starting_sequence[row_index][column_index]
                index += 1




    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence = []
        
        for row in range(rows):
            starting_sequence.append([])
            for col in range(cols):
                starting_sequence[row].append(data_type())

        return Array2D(starting_sequence= starting_sequence, data_type= data_type)


    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        if row_index >= self.row_len:
            raise IndexError("Index too big.")
        return Array2D.Row(row_index, self.array2D, self.column_len, self.data_type) 
    
    def __iter__(self) -> Iterator[Sequence[T]]:
        for num_row in range(self.row_len):
            yield self[num_row]
        
    
    def __reversed__(self):
        for num_row in reversed(range(self.row_len)):
            yield self[num_row]
    
    def __len__(self): 
        return self.row_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.row_len} Rows x {self.column_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')