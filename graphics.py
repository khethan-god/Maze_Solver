from tkinter import Tk, BOTH, Canvas, Label


class Point:
    """Represents a 2D point with x and y coordinates."""
    
    def __init__(self, x, y):
        """Initializes a point with given x and y coordinates."""
        self.x = x
        self.y = y

class Line:
    """Represents a line segment between two points."""
    
    def __init__(self, p1, p2):
        """Initializes a line segment with two endpoints."""
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color='black'):
        """Draws the line on a given canvas with a specified color."""
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Window:
    """Handles the graphical window for the maze visualization."""
    
    def __init__(self, width, height):
        """
        Initializes a window with specified width and height.
        Sets up a Tkinter canvas for drawing the maze.
        """
        self.__window = Tk()
        self.__window.title("Maze Solver")
        self.__window.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__window, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        # Label to display current process info
        self.status_label = Label(self.__window, text="Initializing...", font=("Helvetica", 14))
        self.status_label.pack(side="top", pady=10)

        self.__running = False  # Controls the main event loop

    def update_status(self, text):
        """Updates the label text to show each step"""
        self.status_label.config(text=text)
        self.redraw()

    def redraw(self):
        """Updates the window to reflect any changes in the canvas."""
        self.__window.update_idletasks()
        self.__window.update()

    def draw_line(self, line, fill_color="black"):
        """Draws a line on the canvas."""
        line.draw(self.__canvas, fill_color)
    
    def wait_for_close(self):
        """Keeps the window open until it is closed by the user."""
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        """Closes the window and stops the main loop."""
        self.__running = False