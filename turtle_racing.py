import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black','purple', 'pink', 'brown', 'cyan' ]


# racer = 0
def get_number_of_turtles():
    while True:
        turtles = input("Enter the number of turtles (2 - 10): ")

        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("Input is not numeric ...  Try Again!")
            continue

        if 2 <= turtles <= 10:
            return turtles
        else:
            print("The number of turtles should be between 2 - 10")



def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]




def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20 )
        racer.pendown()
        turtles.append(racer)
    return turtles



def init_turtles():
    screen = turtle.Screen()
    screen.bgcolor("khaki")
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_turtles()
init_turtles()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f" The winner is the turtle with color: {winner}")
time.sleep(5)
