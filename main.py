import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=1000, height=900)
user_bet = screen.textinput(title='Make Your Bets', prompt='Which turtle will win the race ? Enter a color: ')
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
y_position = [400, 330, 260, 190, 120, 50, -20, -90, -160, -230, -300, -370, -440]
turtles_list = []

for turtle_index in range(0, 12):
	new_racer = turtle.Turtle(shape='turtle')
	new_racer.penup()
	new_racer.color(colors[random.randint(0, 5)])
	new_racer.goto(x=-480, y=y_position[turtle_index])
	turtles_list.append(new_racer)

if user_bet:
	is_race_on = True

while is_race_on:

	for racer in turtles_list:
		random_distance = random.randint(0, 10)
		racer.forward(random_distance)
		if racer.xcor() > 480:
			is_race_on = False
			winnig_racer = racer.pencolor()
			if winnig_racer == user_bet:
				print(f"You've won! the {winnig_racer} is winner!")
			else:
				print(f"You've Lose! the {winnig_racer} is winner!")


screen.exitonclick()
