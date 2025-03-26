from graphics import Line, Point


class Cell:
    """Represents a single cell in the maze grid."""
    
    def __init__(self, win=None):
        """
        Initializes a cell with four walls.
        Keeps track of whether the cell has been visited.
        """
        self._x1 = self._y1 = self._x2 = self._y2 = None
        self._win = win
        self.visited = False  # Used during maze generation and solving

        # Initially, all four walls are present
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

    def _draw_wall(self, x1, y1, x2, y2, flag=True):
        """Draws or erases a wall based on the flag value."""
        line = Line(Point(x1, y1), Point(x2, y2))
        color = "black" if flag else "white"
        self._win.draw_line(line, color)

    def draw(self, x1, y1, x2, y2):
        """Draws the cell with its current wall configuration."""
        if self._win is None:
            return
        
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2

        # Draw only the walls that still exist
        self._draw_wall(x1, y1, x1, y2, self.has_left_wall)
        self._draw_wall(x1, y1, x2, y1, self.has_top_wall)
        self._draw_wall(x2, y1, x2, y2, self.has_right_wall)
        self._draw_wall(x1, y2, x2, y2, self.has_bottom_wall)

    def has_none_points(self, other):
        """Check if any coordinate in self or other is None.
        
        Returns:
            bool: True if any coordinate is None, False otherwise.
        """
        return any(getattr(self, attr) is None for attr in ("_x1", "_x2", "_y1", "_y2")) or \
            any(getattr(other, attr) is None for attr in ("_x1", "_x2", "_y1", "_y2"))

    def draw_move(self, to_cell, undo=False):
        """Draws a movement line between this cell and another cell."""
        if self.has_none_points(to_cell):
            return

        fill_color = "gray" if undo else "red"
        
        (x_center, y_center), (x_center2, y_center2) = self.center_line(to_cell)
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)

    def center_line(self, other):
        """Return the center line points of two cells.
        
        Args:
            other (Cell): The other cell to center with.
        
        Returns:
            tuple: The center of the two cells.
        """
        x_center = self._x1 + (self._x2 - self._x1) // 2
        y_center = self._y1 + (self._y2 - self._y1) // 2
        x_center2 = other._x1 + (other._x2 - other._x1) // 2
        y_center2 = other._y1 + (other._y2 - other._y1) // 2
        return (x_center, y_center), (x_center2, y_center2)
    

        
        # Horizontal movement self(x1+x2)/2 to to_cell(x1+x2)/2, (y1, y2) same
        # Veritcal movement self(y1+y2)/2 to to_cell(y1+y2)/2, (x1, x2) same
        # OR
        # half_length = abs(self._x2 - self._x1) // 2
        # x_center = half_length + self._x1
        # y_center = half_length + self._y1

        # half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        # x_center2 = half_length2 + to_cell._x1
        # y_center2 = half_length2 + to_cell._y1