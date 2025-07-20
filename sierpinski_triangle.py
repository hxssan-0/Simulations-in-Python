import turtle
import math

#the pts A, B and C of the original triangle
def sierpinski(x1, y1, x2, y2, x3, y3, t):
    mid_ab = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
    mid_bc = ((x2 + x3) / 2.0, (y2 + y3) / 2.0)
    mid_ac = ((x1 + x3) / 2.0, (y1 + y3) / 2.0)
    d = math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))

    if d > 10:
        sierpinski(x1, y1, mid_ab[0], mid_ab[1], mid_ac[0], mid_ac[1], t)
        sierpinski(mid_ab[0], mid_ab[1], x2, y2, mid_bc[0], mid_bc[1], t)
        sierpinski(mid_ac[0], mid_ac[1], mid_bc[0], mid_bc[1], x3, y3, t)
    else:
        t.up()
        #draw the triangle
        t.setpos(x1, y1)
        t.down()
        t.setpos(x2, y2)
        t.setpos(x3, y3)
        t.setpos(x1, y1)
        t.up()

def main():
    t = turtle.Turtle()
    t.hideturtle()
    sierpinski(-200, -100, 0, 200, 200, -100, t)
    turtle.Screen().exitonclick()

main()