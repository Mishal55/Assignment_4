
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Eraser on Canvas")

# Define the canvas size and grid size
canvas_width = 500
canvas_height = 500
grid_size = 20
eraser_size = 40  # The size of the eraser in pixels

# Create a canvas widget
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Draw the grid of blue cells
cells = {}
for x in range(0, canvas_width, grid_size):
    for y in range(0, canvas_height, grid_size):
        cell = canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill="blue", outline="blue")
        cells[cell] = (x, y)

# Create an eraser rectangle (initial position)
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="white", outline="black")

# Function to move the eraser and erase cells
def move_eraser(event):
    # Get the current mouse position
    mouse_x, mouse_y = event.x, event.y

    # Move the eraser to the mouse position, constrained by the grid size
    canvas.coords(eraser, mouse_x - eraser_size / 2, mouse_y - eraser_size / 2,
                  mouse_x + eraser_size / 2, mouse_y + eraser_size / 2)

    # Erase the cells that are touched by the eraser
    for cell, (cell_x, cell_y) in cells.items():
        # Check if the eraser overlaps with the cell
        if (cell_x < mouse_x < cell_x + grid_size and
            cell_y < mouse_y < cell_y + grid_size):
            canvas.itemconfig(cell, fill="white")

# Bind the mouse movement to move the eraser
canvas.bind("<B1-Motion>", move_eraser)

# Start the Tkinter event loop
root.mainloop()
