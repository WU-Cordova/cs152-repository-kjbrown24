class Cell:
    def __init__(self, is_alive: bool = False) -> None:
        """
        Creates a cell and sets its initial state (alive or dead).
        :param is_alive: True if the cell is alive, False if it's dead (default is False).
        """
        self.alive = is_alive

    def num_neighbors(self):
        """
        Placeholder for counting neighbors (not used here, but can be added later if needed).
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Checks if this cell is the same as another cell (based on being alive or dead).
        :param other: Another cell to compare
        :return: True if both cells have the same state, False otherwise
        """
        return self.alive == other.alive

    def __str__(self) -> str:
        """
        Returns a string to visually represent the cell.
        :return: A skull (💀) if the cell is dead, or bacteria (🦠) if the cell is alive
        """
        return "💀" if not self.is_alive else "🦠"

    @property
    def is_alive(self) -> bool:
        """
        Gets whether the cell is alive.
        :return: True if the cell is alive, False otherwise
        """
        return self.alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        """
        Sets whether the cell is alive.
        :param is_alive: True to make the cell alive, False to make it dead
        """
        self.alive = is_alive