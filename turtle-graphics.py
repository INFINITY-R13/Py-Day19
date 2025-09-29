# turtle-graphics.py

"""
A simple Etch-A-Sketch game using Python's Turtle graphics.

Controls:
- W: Move forward
- S: Move backward
- A: Turn left (counter-clockwise)
- D: Turn right (clockwise)
- C: Clear the screen and reset the turtle to the center
"""

# Import necessary classes from the turtle module.
from turtle import Turtle, Screen

# --- INITIALIZATION ---
# Create a turtle object, which is our "pen".
tim = Turtle()
# Create a screen object, which is our "canvas".
screen = Screen()

# --- MOVEMENT FUNCTIONS ---
# Each function controls a specific movement for the turtle.

def move_forward():
    """Moves the turtle forward by 10 units."""
    tim.forward(10)

def move_backward():
    """Moves the turtle backward by 10 units."""
    tim.backward(10)

def turn_left():
    """Turns the turtle 10 degrees to the left."""
    tim.left(10)

def turn_right():
    """Turns the turtle 10 degrees to the right."""
    tim.right(10)

def clear_drawing():
    """Clears all drawings, resets the turtle's position and orientation."""
    tim.clear()       # Clears the drawings made by this turtle.
    tim.penup()       # Lifts the pen to avoid drawing during repositioning.
    tim.home()        # Moves the turtle to the origin (0,0).
    tim.pendown()     # Puts the pen down to be ready for drawing again.

# --- EVENT LISTENERS ---
# Set up the screen to start listening for keyboard events.
screen.listen()

# Bind keystrokes to the corresponding functions.
# The `onkey()` method takes a key and a function to call when that key is pressed.
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

# --- EXIT ---
# Keep the window open until the user clicks on the screen.
screen.exitonclick()
