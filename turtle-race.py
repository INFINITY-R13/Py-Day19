# turtle-race.py

# Import necessary classes from the turtle module and the random module.
from turtle import Turtle, Screen
import random

# --- SCREEN SETUP ---
# Initialize a new screen object.
screen = Screen()
# Set the dimensions of the screen window.
screen.setup(width=500, height=400)

# --- USER BET ---
# Create a text input dialog to ask the user for their bet.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Guess a color: ")

# --- SETUP TURTLES ---
# Define the list of colors for the turtles.
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# Define the starting y-coordinates for each turtle.
y_positions = [-70, -40, -10, 20, 50, 80]
# Create an empty list to hold all the turtle instances.
all_turtles = []

# Loop to create and position the six turtles.
for turtle_index in range(0, 6):
    # Create a new turtle with the "turtle" shape.
    new_turtle = Turtle(shape="turtle")
    # Lift the pen so it doesn't draw a line when moving.
    new_turtle.penup()
    # Assign a color from the colors list.
    new_turtle.color(colors[turtle_index])
    # Move the turtle to its starting position on the left edge of the screen.
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # Add the newly created turtle to our list.
    all_turtles.append(new_turtle)

# --- RACE LOGIC ---
# A flag to control the main race loop.
is_race_on = False

# The race will only start if the user has entered a bet.
if user_bet:
    is_race_on = True

# Main game loop. Continues as long as the race is on.
while is_race_on:
    # Loop through each turtle in our list.
    for turtle in all_turtles:
        # Check if a turtle has reached the finish line.
        # The screen width is 500, so the x-coordinate ranges from -250 to 250.
        # The finish line is set at x=230.
        if turtle.xcor() > 230:
            # Stop the race.
            is_race_on = False
            # Get the color of the winning turtle.
            winning_color = turtle.pencolor()
            # Compare the winning color with the user's bet.
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            # **BUG FIX**: Added 'break' to exit the for loop immediately.
            # Without this, other turtles would move one more time even after a winner is declared.
            break

        # Generate a random distance for the turtle to move forward.
        random_distance = random.randint(0, 10)
        # Move the turtle forward by the random distance.
        turtle.forward(random_distance)

# --- EXIT ---
# The screen will close only when the user clicks on it.
screen.exitonclick()
