#complete
#program.py
from projects.project2.Grid import Grid
from projects.project2.Gamecontroller import Gamecontroller
def main():
    grid = Grid(10,10)
    game_control = Gamecontroller(grid)
    game_control.run(100)
    #pass



if __name__ == '__main__':
    main()