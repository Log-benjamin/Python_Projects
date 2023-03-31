from turtle import Turtle, Screen
import random


All_Turtles = []
race = False
count = -100
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=600, height=600)
user = screen.textinput(title="Make your bet.",
                        prompt="Which Turtle will win the Race? R, O, Y, G, B, P - Enter a color : ")


for z in range(0, 6):
    new_T = Turtle(shape="turtle")
    new_T.color(colors[z])
    new_T.penup()
    new_T.goto(x=-290, y=count)
    count += 40
    All_Turtles.append(new_T)


if user:
    race = True


while race:
    for T in All_Turtles:
        if T.xcor() > 280:
            race = False
            winner = T.pencolor()
            if winner == user:
                print(f"You have Won! The {winner} turtle is the winner")
                T.pencolor("Black")
                T.write("You Won", align="right", move=False, font=("Arial", 15, 'normal', 'bold', 'italic'))
            else:
                print(f"You have lost! The {winner} turtle is the winner")
                T.pencolor("Black")
                T.write("You Lost", align="right", move=False, font=("Arial", 15, 'normal', 'bold', 'italic'))
        speed = random.randint(0, 10)
        T.fd(speed)


screen.exitonclick()
