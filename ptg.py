import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

# t.color('red')
# t.begin_fill()
# t.circle(90)
# t.end_fill()

# for _ in range(20):
#     t.left(10)
#     t.forward(50)
#     t.left(10)
#     t.backward(50)

# leonardo = turtle.Turtle()
# raphael = turtle.Turtle()
# donatelo = turtle.Turtle()
# miki = turtle.Turtle()

# leonardo.color('blue')
# leonardo.forward(90)
# leonardo.left(90)
# leonardo.forward(90)

# raphael.color('red')
# raphael.right(90)
# raphael.forward(90)

# miki.color('orange')
# miki.left(90)
# miki.forward(125)


# donatelo.color('purple')
# donatelo.left(180)
# donatelo.forward(120)
# donatelo.left(90)
# donatelo.forward(32)

class DrawShape:
    def draw(self, sides, angle):
        for distance in sides:
            t.forward(distance)
            t.left(angle)

class Rectangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90

class Triangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 120

# square = Rectangle([90]*4)
triangle = Triangle([100]*3)
triangle.draw(triangle.sides, triangle.angle)
screen.mainloop()