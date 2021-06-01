#kochDrawV1.py
import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
def main():
    t.setup(800,500)
    t.pu()
    t.goto(-300,50)
    t.pd()
    t.pensize(3)
    t.speed(0)
    #level = 3
    for i in range(3):
       koch(300,3)
       t.right(120)
       if i >3:break
    #t.hideturtle()
    t.done()

main()