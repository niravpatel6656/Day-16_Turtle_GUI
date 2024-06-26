import turtle
from turtle import Turtle, Screen
import random
# Create a turtle object
t = Turtle()
t.color("green")
t.width(2)
t.shape("circle")
t.speed(0)
turtle.colormode(255)
# Function to generate colors

def color_gen():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



angle_list = ["0","90","180","270"]

# Random Walk
# for _ in range(0,100):
#     t.color(color_gen())
#     t.forward(25)
#     t.left(int(random.choice(angle_list)))

# Spirograph
for _ in range(0,121):
    t.color(color_gen())
    t.circle(100)
    t.left(3)

# Combine Shape
# for i in range(3,10):
#     t.color(random.choice(color_list))
#     for _ in range(i):
#         angle = 180 - (((i-2)*180)/i)
#         t.forward(100)
#         t.left(angle)

# Triangle
# for _ in range(3):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(120)


# Square
# for _ in range(4):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(90)

# Pentagon
# for _ in range(5):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(72)


# Hexagon
# for _ in range(6):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(60)

# Heptagon
# for _ in range(7):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(51.43)

# Octagon
# for _ in range(8):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(45)

# Nonagon
# for _ in range(9):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(40)

# Decagon
# for _ in range(10):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(36)



s = Screen()
s.exitonclick()
