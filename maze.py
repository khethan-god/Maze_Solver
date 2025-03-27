import time
import random
from cell import Cell


class Maze:
    """Generates and solves a maze using Graph traversal approach."""
    
    def __init__(self, x1, y1, rows, cols, cell_size_x, cell_size_y, win=None, seed=None):
        """
        Initializes a maze with given dimensions and grid size.
        Generates the maze using a recursive backtracking algorithm.
        """
        self._cells = []
        self._x1, self._y1 = x1, y1
        self._num_rows, self._num_cols = rows, cols
        self._cell_size_x, self._cell_size_y = cell_size_x, cell_size_y
        self._win = win

        if seed:
            random.seed(seed)  # Ensures reproducibility
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)  # Recursive backtracking
        self._reset_cells_visited()

    def _create_cells(self):
        """Creates the maze grid and draws each cell."""
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                self._win.update_status(f"Creating cell ({i+1}, {j+1})")

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        """Removes the top-left and bottom-right walls to create an entry and exit."""
        self._win.update_status("Breaking walls...")
        time.sleep(0.02)
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

        # since we are breaking these after creating the walls, just change its
        # color from black to white, because the walls are already drawn

    def _break_walls_r(self, i, j):
        """Recursively removes walls to generate a random maze."""
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                next_index_list.append((i+1, j))
            # up
            if j > 0 and not self._cells[i][j-1].visited:
                next_index_list.append((i, j-1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                next_index_list.append((i, j+1))

            # if there are no unvisited neighbors, return
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            # choose one of the unvisited neighbors at random
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # remove the wall between the current cell and the chosen cell
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
           
            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def neighbors(self, i, j):
        neighbors = []
        for x, y, side in [(i - 1, j, "left"), (i + 1, j, "right"), (i, j - 1, "top"), (i, j + 1, "bottom")]:
            # Check bounds and wall conditions
            if 0 <= x < self._num_cols and 0 <= y < self._num_rows:
                if not self._cells[x][y].visited and not eval(f"self._cells[i][j].has_{side}_wall"):
                    neighbors.append((x, y))
        return neighbors
    
    # Returns True if this is the end cell, OR if it leads to the end cell.
    # Returns False if this is a "loser" cell (a dead-end).
    def _solve_dfs_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if (i, j) == (self._num_cols - 1, self._num_rows - 1):
            return True

        # use DFS on each neigbor if present
        neighbor = self.neighbors(i, j)
        for x, y in neighbor:
        # moves left/right/up/down if there is no wall and it hasn't been visited
            self._cells[i][j].draw_move(self._cells[x][y])
            if self._solve_dfs_r(x, y):
                return True
            self._cells[i][j].draw_move(self._cells[x][y], True)

        # we went the wrong way let the previous cell know by returning False
        return False
                
    def _solve_bfs_r(self, i, j):
        return self._solve_bfs_i(i, j) # its better this way


    def _solve_dfs_i(self, i, j):
        self._animate()
        stack = [(i, j)]

        while stack:
            i, j = stack.pop()
            if not self._cells[i][j].visited:
                self._cells[i][j].visited = True

            if (i, j) == (self._num_cols - 1, self._num_rows - 1):
                return True

            for x, y in self.neighbors(i, j):
                stack.append((x, y))
                self._cells[i][j].draw_move(self._cells[x][y])

        return False
    
    def _solve_bfs_i(self, i, j):
        self._animate()
        stack = [(i, j)] # queue for the iterative BFS

        while stack:
            i, j = stack.pop(0)
            
            # Mark the current cell as visited
            if not self._cells[i][j].visited:
                self._cells[i][j].visited = True

            # If we are at the end cell, return True
            if (i, j) == (self._num_cols - 1, self._num_rows - 1):
                return True

            # Check neighbors and push them to the stack
            for x, y in self.neighbors(i, j):
                stack.append((x, y))
                self._cells[i][j].draw_move(self._cells[x][y])

        # If the stack is empty and we haven't found the solution, return False
        return False

    # create the moves for the solution using a user specified approach
    def solve(self, method='dfs', approach='i'):
        self._win.update_status("Solving maze...")
        return eval(f"self._solve_{method}_{approach}(0, 0)")
    
    def on_solved(self):
        self._win.update_status("Maze Solved!")
        self._celebrate()

    def _celebrate(self):
        """Simulate celebration when the maze is solved."""
        for _ in range(5):
            self._win.update_status("◝(ᵔᗜᵔ)◜(っᵔ◡ᵔ)っ Maze Solved! ◝(ᵔᗜᵔ)◜(っᵔ◡ᵔ)っ")
            time.sleep(0.25)
            self._win.update_status("◝(ᵔᗜᵔ)৻(  •̀ ᗜ •́  ৻) Maze Solved! ◝(ᵔᗜᵔ)৻(  •̀ ᗜ •́  ৻)")
            time.sleep(0.25)
        self._win.update_status("Great Job!")