import turtle
import pandas

SCORE = 0

screen = turtle.Screen()

screen.title("Us States Name Guess")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
data_states = data.state.to_list()

while SCORE < 50:
    answer = screen.textinput(title=f"{SCORE}/50 states completed!", prompt="What's another state name? ").title()

    if answer == "Exit":
        break

    if answer in data_states:
        SCORE += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        individual_state = data[data.state == answer]
        t.goto(int(individual_state.x), int(individual_state.y))
        t.write(answer)

screen.exitonclick()
