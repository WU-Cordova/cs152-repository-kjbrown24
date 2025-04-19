#complete
#program.py
from projects.project2.Grid import Grid
from projects.project2.Gamecontroller import Gamecontroller

def main():
    """
    Sets up the game and starts the simulation.
    - Creates a grid with 10 rows and 10 columns.
    - Initializes the game controller with the grid.
    - Runs the simulation for up to 100 generations.
    """
    grid = Grid(10, 10)  # Create a 10x10 grid with random cells
    game_control = Gamecontroller(grid)  # Set up the game controller with the grid
    game_control.run(100)  # Run the simulation for up to 100 generations

if __name__ == '__main__':
    """
    Starts the program by calling the main function.
    """
    main()