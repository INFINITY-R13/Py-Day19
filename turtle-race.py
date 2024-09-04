from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Guess a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple' ]
y_axis = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(x=-230, y=y_axis[turtle_index])

screen.exitonclick()