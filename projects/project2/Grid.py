#Grid.py
from __future__ import annotations
import copy
from datastructures.array2d import Array2D
from datastructures.array import Array
from projects.project2.Cell import Cell
import random
from typing import List


class Grid:
    def init(self, width: int, height: int) -> None:
        cells = []

        for row in range(width):
            cells.append([])
            for col in range(height):
                alive = random.choice([True, False])
                cells[row].append(Cell(is_alive = alive))
        self.grid = Array2D(starting_sequence= cells,data_type= Cell)
        self.row_size = width
        self.col_size = height

    def num_alive(self) -> int:
        count = 0
        for row in self.grid:
            for cell in row:
                if cell.alive:
                    count += 1
        return count
    def num_neighbors(self, row_index: int, col_index: int) -> int:
        count = 0
        # for row in range(len(self.grid)):
        #     for col in range(len(self.grid[0])):
        for row in range(row_index -1, row_index +2):
             for col in range(col_index-1, col_index +2):
                  if (row == row_index and col == col_index) or not (0 <= row < self.row_size and 0 <= col < self.col_size):
                       continue
                  if self.grid[row][col].alive:
                       count += 1
        return count
    def next_gen(self) -> Grid:
        new_grid = copy.deepcopy(self.grid)
        for row in range(len(self.grid)):
             for col in range(len(self.grid[0])):
                neighbors = self.num_neighbors(row,col)
                if neighbors == 2:
                        new_grid[row][col].alive = self.grid[row][col].alive
                elif neighbors == 3:
                        new_grid[row][col].alive = True
                else:
                    new_grid[row][col].alive = False
        grid_object = Grid(self.row_size, self.col_size)
        grid_object.grid = new_grid
        return grid_object

    def __eq__(self, other: object) -> bool:
         if not isinstance(other, Grid):
              return False
         return self.grid == other.grid

    def display(self):
        for row in range(self.row_size):
            for col in range(self.col_size):
                  print(self.grid[row][col], end='')
            print() 

    def str(self):
        for row in self.grid:
            print(row)
            # for col in self.grid:
            #     print(self.cells)
        return ''

                
        