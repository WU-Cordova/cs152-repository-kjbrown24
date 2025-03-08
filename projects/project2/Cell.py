#Cell.py
class Cell:
    def init(self, is_alive: bool = False) -> None:
        self.alive = is_alive
        # self.loc = (int, int)

    def num_neighbors(self):
        pass

    def eq(self, other: object) -> bool:
        return self.alive == other.alive

    def str__(self):
        if self.is_alive == False:
            return "💀"
        else:
            return "🦠"
    @property
    def is_alive(self) -> bool:
        return self.alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self.alive = is_alive