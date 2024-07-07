import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)  
t.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

def draw(radius, num_circles):
    for i in range(num_circles):
        t.pencolor(colors[i % len(colors)])  
        t.circle(radius)
        t.left(360 / num_circles)

for j in range(20, 200, 20):
    draw(j, 36)

t.hideturtle()
turtle.done()
