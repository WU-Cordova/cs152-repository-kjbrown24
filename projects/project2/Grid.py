from __future__ import annotations
import copy
from datastructures.array2d import Array2D
from datastructures.array import Array
from projects.project2.Cell import Cell
import random
from typing import List


class Grid:
    def __init__(self, width: int, height: int) -> None:
        """
        Sets up the grid with a random pattern of alive or dead cells.
        :param width: Number of rows in the grid
        :param height: Number of columns in the grid
        """
        # Create an empty grid of cells
        cells = []
        for row in range(width):
            cells.append([])
            for col in range(height):
                # Decide randomly if a cell is alive or dead
                alive = random.choice([True, False])
                cells[row].append(Cell(is_alive=alive))
        # Store the cells in a 2D array
        self.grid = Array2D(starting_sequence=cells, data_type=Cell)
        self.row_size = width  # Number of rows
        self.col_size = height  # Number of columns

    def num_alive(self) -> int:
        """
        Counts how many cells in the grid are alive.
        :return: Number of live cells
        """
        count = 0
        # Go through each row and cell in the grid
        for row in self.grid:
            for cell in row:
                if cell.alive:  # If the cell is alive, add to the count
                    count += 1
        return count

    def num_neighbors(self, row_index: int, col_index: int) -> int:
        """
        Finds the number of live neighbors around a cell.
        :param row_index: Row location of the cell
        :param col_index: Column location of the cell
        :return: Number of live neighbors
        """
        count = 0
        # Check the eight spots around the cell
        for row in range(row_index - 1, row_index + 2):
            for col in range(col_index - 1, col_index + 2):
                # Skip the cell itself and spots outside the grid
                if (row == row_index and col == col_index) or not (0 <= row < self.row_size and 0 <= col < self.col_size):
                    continue
                if self.grid[row][col].alive:  # If the neighbor is alive, add to the count
                    count += 1
        return count

    def next_gen(self) -> Grid:
        """
        Calculates what the grid will look like in the next generation.
        :return: A new grid with updated cells
        """
        # Copy the current grid to avoid changing it directly
        new_grid = copy.deepcopy(self.grid)
        # Go through each cell and apply the rules
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                neighbors = self.num_neighbors(row, col)  # Count live neighbors
                if neighbors == 2:
                    # Keep the cell the way it is
                    new_grid[row][col].alive = self.grid[row][col].alive
                elif neighbors == 3:
                    # Cell becomes or stays alive
                    new_grid[row][col].alive = True
                else:
                    # Cell dies or stays dead
                    new_grid[row][col].alive = False
        # Create and return a new Grid object with the updated cells
        grid_object = Grid(self.row_size, self.col_size)
        grid_object.grid = new_grid
        return grid_object

    def __eq__(self, other: object) -> bool:
        """
        Compares two grids to see if they are exactly the same.
        :param other: Another grid to compare to
        :return: True if the grids are identical, False otherwise
        """
        if not isinstance(other, Grid):  # If it's not even a Grid object, return False
            return False
        return self.grid == other.grid  # Compare the grids directly

    def display(self):
        """
        Prints the grid to the screen so you can see it.
        """
        for row in range(self.row_size):
            for col in range(self.col_size):
                print(self.grid[row][col], end='')  # Print each cell
            print()  # Move to the next row

    def str(self):
        """
        Turns the grid into a string for debugging.
        :return: A string version of the grid
        """
        for row in self.grid:
            print(row)  # Print each row
        return ''

                
        