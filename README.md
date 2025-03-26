# Maze Generator and Solver

## Overview
This Python project generates and solves a maze using the depth-first search (DFS) algorithm. The maze is displayed using Tkinter, where each cell in the grid represents a segment of the maze. The program first creates a grid, carves out a solvable maze using a recursive backtracking algorithm, and then attempts to solve it visually.

## Features
- Generates a random maze using a recursive backtracking approach.
- Visual representation using Tkinter.
- Solves the maze using depth-first search (DFS) with an animated path.
- Adjustable grid size, cell dimensions, and seed for reproducibility.

## Installation
Ensure you have Python installed (>=3.10). No additional dependencies are required as the project uses standard libraries.

### Steps:
1. Clone the repository or download the script:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Run the script:
   ```sh
   ./main.sh
   ```

## Usage
- The script will open a graphical window displaying the maze generation process.
- Once the maze is created, it will be solved automatically using DFS.
- The solution path is drawn in red, and backtracking moves (if required) are shown in gray.
- The window remains open until the user closes it.

## Configuration
You can modify the following parameters in the `main()` function:
- `num_rows`: Number of rows in the maze grid.
- `num_cols`: Number of columns in the maze grid.
- `screen_x`, `screen_y`: Window dimensions.
- `seed`: Random seed for maze reproducibility.

Example:
```python
num_rows = 12
num_cols = 16
seed = 42  # Fixed seed for consistent maze generation
```

## How It Works
### Maze Generation
1. The program initializes a grid of cells.
2. A recursive backtracking algorithm is used to carve out paths by removing walls between adjacent cells.
3. Entry and exit points are set at the top-left and bottom-right corners.

### Maze Solving
1. A depth-first search (DFS) algorithm starts from the entrance.
2. It marks visited cells and moves recursively in available directions.
3. The correct path is visualized in red, while backtracking is shown in gray.
4. The search stops when the exit is reached.

## Troubleshooting
- If the maze appears unresponsive, try increasing the recursion limit:
  ```python
  sys.setrecursionlimit(10000)
  ```
- If the window does not display properly, ensure your Tkinter installation is functional.
- If performance issues arise, consider reducing the grid size (`num_rows`, `num_cols`).

## License
This project is licensed under the MIT License.

## Acknowledgments
- Inspired by common recursive maze generation techniques.
- Implemented using Python's Tkinter for visualization.

