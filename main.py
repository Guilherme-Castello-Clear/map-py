import turtle

screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess the State", prompt="What's another state's name? ")
print(answer_state)
