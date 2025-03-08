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
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError("Column index out of range.")
            index = self.map_index(self.row_index, column_index)
            return self.array[index]

        def map_index(self, row_index, column_index):
            return row_index * self.num_columns + column_index

        def __setitem__(self, column_index: int, value: T) -> None:
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError("Column index out of range.")
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value

        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]

        def __reversed__(self) -> Iterator[T]:
            for col_num in reversed(range(self.num_columns)):
                yield self[col_num]

        def __len__(self) -> int:
            return self.num_columns

        def __str__(self) -> str:
            return f"[{', '.join(str(self[column_index]) for column_index in range(self.num_columns))}]"

        def __repr__(self) -> str:
            return f"Row {self.row_index}: {self.__str__()}"


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Entered sequence is not a sequence.")

        for row in starting_sequence:
            if not isinstance(row, Sequence):
                raise ValueError("Each row must be a sequence.")
            for item in row:
                if not isinstance(item, data_type):
                    raise ValueError("All items must be of the specified data type.")

        self.data_type = data_type
        self.row_len = len(starting_sequence)
        self.column_len = len(starting_sequence[0])

        for row in starting_sequence:
            if len(row) != self.column_len:
                raise ValueError("All rows must have the same length.")

        self.array2D = Array([data_type() for _ in range(self.row_len * self.column_len)], data_type=data_type)

        index = 0
        for row_index in range(self.row_len):
            for column_index in range(self.column_len):
                self.array2D[index] = starting_sequence[row_index][column_index]
                index += 1

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        return Array2D(starting_sequence=[[data_type() for _ in range(cols)] for _ in range(rows)], data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        if row_index < 0 or row_index >= self.row_len:
            raise IndexError("Row index out of range.")
        return Array2D.Row(row_index, self.array2D, self.column_len, self.data_type)

    def __iter__(self) -> Iterator[Sequence[T]]:
        for row_index in range(self.row_len):
            yield self[row_index]

    def __reversed__(self) -> Iterator[Sequence[T]]:
        for row_index in reversed(range(self.row_len)):
            yield self[row_index]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array2D) or len(self.array2D) != len(other.array2D):
            return False
        return all(self.array2D[i] == other.array2D[i] for i in range(len(self.array2D)))

    def __len__(self): 
        return self.row_len

    def __str__(self) -> str: 
        return f'[{", ".join(str(row) for row in self)}]'

    def __repr__(self) -> str: 
        return f'Array2D {self.row_len} Rows x {self.column_len} Columns, items: {self.__str__()}'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')