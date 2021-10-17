import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

class House():
    def draw(self, size):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.penup()
        t.left(90)
        t.forward(size)
        t.pendown()
        t.right(30)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.penup()
        t.right(30)
        t.forward(size)
        t.right(90)
        t.pendown()
        t.forward(size / 5)
        t.right(90)
        t.forward(size / 5)
        t.left(90)
        t.forward(size / 6)
        t.left(90)
        t.forward(size / 5)
house = House()
house.draw(100)
screen.mainloop()