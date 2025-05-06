import time
from datastructures.array2d import Array2D
from projects.project2.Grid import Grid
from projects.project2.kbhit import KBHit

class Gamecontroller:
    def __init__(self, grid: Grid) -> None:
        """
        Sets up the game controller.
        :param grid: The starting grid for the simulation
        """
        print("Game controller is ready!")
        self.grid = grid  # The current grid
        self.history = []  # Keeps track of past grids

    def run(self, max_iter: int) -> None:
        """
        Runs the Game of Life simulation.
        :param max_iter: Maximum number of generations to simulate
        """
        kb = KBHit()  # For keyboard controls
        print("Press (Q) to quit, (S) for step mode, or (C) to continue auto mode.")

        generation = 0  # Start generation counter
        step_mode = False  # Step-by-step mode is off at the start

        # Keep running the simulation until the user quits or the grid stabilizes
        while True or generation < max_iter:
            print(f'Generation: {generation}')
            generation += 1

            # Show the current grid
            self.grid.display()
            time.sleep(1)  # Pause for 1 second (for auto mode)

            # Add the current grid to the history
            self.history.append(self.grid)

            # Create the next generation grid
            new_grid = self.grid.next_gen()

            # If the history gets too big, check for stability or repetition
            if len(self.history) > 5:
                # Stop if the grid is the same as any recent grid
                if self.history[-1] == new_grid or self.history[-2] == new_grid or self.history[-3] == new_grid:
                    break
                # Remove the oldest grid from history to save space
                del self.history[0]

            # Update the grid to the new generation
            self.grid = new_grid

            # Check if a key is pressed or if we're in step mode
            if kb.kbhit() or step_mode:
                c = (kb.getch()).upper()  # Get the pressed key and convert to uppercase
                print(c)
                time.sleep(2)  # Small delay for smoother interaction

                # Stop the simulation if 'Q' is pressed
                if c == 'Q':
                    break

                # Enter step mode if 'S' is pressed
                if c == 'S':
                    step_mode = True

                # Go back to auto mode if 'C' is pressed
                if c == 'C':
                    step_mode = False

        # Finish the simulation and reset terminal settings
        print("Simulation ended. The cells are no more!")
        kb.set_normal_term()

