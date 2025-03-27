# Maze Generator and Solver

## Overview
This Python project generates and solves a maze using either the Depth-First Search (DFS) or Breadth-First Search (BFS) algorithm. The maze is displayed using Tkinter, where each cell in the grid represents a segment of the maze. The program first creates a grid, carves out a solvable maze using a recursive backtracking algorithm, and then attempts to solve it using the chosen algorithm, either DFS or BFS, with an animated path.

## Features
- Generates a random maze using a recursive backtracking algorithm.
- Visual representation using Tkinter.
- Solves the maze using DFS or BFS with an animated path.
- Adjustable grid size, cell dimensions, and seed for reproducibility.
- Allows choice between DFS and BFS for solving, and supports both iterative and recursive DFS approaches.

## Installation
Ensure you have Python installed (>=3.10). No additional dependencies are required as the project uses standard libraries.

### Steps:
1. Clone the repository or download the script:
   ```sh
   git clone https://github.com/khethan-god/Maze_Solver.git
   cd Maze_Solver
   ```
2. Run the script:
   ```sh
   ./main.sh
   ```

## Usage
- The script will open a graphical window displaying the maze generation process.
- Once the maze is created, it will be solved automatically using the algorithm specified.
- The solution path is drawn in red, and backtracking moves (if required) are shown in gray.
- The window remains open until the user closes it.

## Solving the Maze
Certainly! Below is an updated and improved version of the README that incorporates the changes you requested, while ensuring grammatical and theoretical correctness:

---

# Maze Generator and Solver

## Overview
This Python project generates and solves a maze using either the **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** algorithm. The maze is displayed using **Tkinter**, where each cell in the grid represents a segment of the maze. The program first creates a grid, carves out a solvable maze using a recursive backtracking algorithm, and then attempts to solve it using the chosen algorithm, either DFS or BFS, with an animated path.

## Features
- Generates a random maze using a **recursive backtracking** algorithm.
- Visual representation using **Tkinter**.
- Solves the maze using **DFS** or **BFS** with an animated path.
- Adjustable grid size, cell dimensions, and seed for reproducibility.
- Allows choice between DFS and BFS for solving, and supports both iterative and recursive DFS approaches.
  
## Installation
Ensure you have Python installed (>=3.10). No additional dependencies are required as the project uses standard libraries.

### Steps:
1. Clone the repository or download the script:
   ```sh
   git clone https://github.com/khethan-god/Maze_Solver.git
   cd Maze_Solver
   ```
2. Run the script:
   ```sh
   ./main.sh
   ```

## Usage
- The script will open a graphical window displaying the maze generation process.
- Once the maze is created, it will be solved automatically using the algorithm specified.
- The solution path is drawn in **red**, and backtracking moves (if required) are shown in **gray**.
- The window remains open until the user closes it.
  
## Solving the Maze
You can choose between two algorithms for solving the maze: **DFS** and **BFS**. These algorithms can be selected by passing them as string parameters to the `solve()` method of the `Maze` class. For example:

```python
maze.solve("dfs")   # Use DFS to solve the maze
maze.solve("bfs")   # Use BFS to solve the maze
```

### DFS (Depth-First Search)
- **DFS Recursive**: If you want to visualize how DFS works step by step and explore the maze in depth, you can use the recursive version of DFS. This method explores one path as deeply as possible before backtracking.
  
  ```python
  maze.solve("dfs", "r")  # Uses recursive DFS method
  ```

- **DFS Iterative**: If you simply want to see the solution path (without the depth-first exploration), you can use the iterative DFS method. This version of DFS solves the maze without explicitly using recursion and is more efficient in terms of stack space.

  ```python
  maze.solve("dfs", "r")  # Uses iterative DFS method
  ```

### BFS (Breadth-First Search)
- **BFS Iterative**: This method solves the maze by exploring all possible neighbors level by level, ensuring that the shortest path is found. BFS uses a queue to explore nodes in a breadth-first manner. Note that BFS is implemented only iteratively, as recursion is not suitable for BFS due to the nature of the algorithm. Recursion in BFS doesn’t provide a clear repeating pattern, which makes it inefficient and unnecessary.

  ```python
  maze.solve("bfs")  # Uses iterative BFS method
  ```

> _**Note**_: For BFS, no recursive solution is implemented because it doesn’t make sense to write BFS using recursion. The BFS algorithm inherently works level by level, which fits naturally with an iterative approach using a queue. Recursion, on the other hand, is typically more suited for algorithms that explore deep paths (such as DFS), where the system needs to backtrack and explore different branches of the search space.

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
1. The program initializes a grid of cells.
2. A **recursive backtracking** algorithm is used to carve out paths by removing walls between adjacent cells.
3. Entry and exit points are set at the top-left and bottom-right corners.
4. A **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** algorithm starts from the entrance and explores the maze.
5. It marks visited cells and moves through the maze, exploring one path at a time.
6. The correct path is visualized in **red**, while backtracking is shown in **gray**.
7. The search stops when the exit is reached, either by finding a solution path in DFS or exploring all neighbors in BFS.

## Troubleshooting
- If the maze appears unresponsive, try increasing the recursion limit if you are using the recursive approach:
  ```python
  sys.setrecursionlimit(10000)
  ```
- If the window does not display properly, ensure your **Tkinter** installation is functional.
- If performance issues arise, consider reducing the grid size (`num_rows`, `num_cols`).

## License
This project is licensed under the **MIT License**.

## Acknowledgments
- Thanks to [boot.dev](https://boot.dev/)