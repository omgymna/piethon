
import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed(0)


screen = t.Screen()
screen.title("Jimena's Turtle Game")



def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    my_tuple = (r,g,b)

    return my_tuple

def draw_random_walk():

    directions = [0, 90, 180, 270]
    direction = random.choice(directions)
    

    for _ in range(100):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.left(direction)
        direction = random.choice(directions)

def draw_spirograph():
    num_circles = random.randint(0,100)
    angle = 360 / num_circles
    radius = random.randint(30,150)
    
    for _ in range(num_circles):
        timmy.color(random_color())
        timmy.circle(radius)
        timmy.left(angle)

choice = input("Do you want to draw shapes, a random walk, or a spirograph? (shapes/walk/spiral): ")

if choice == 'shapes':
    draw_shape()
elif choice == 'walk':
    draw_random_walk()
else:
    draw_spirograph()

screen.exitonclick()
