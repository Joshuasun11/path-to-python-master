#snake.py
import turtle as t
t.setup(350,350,200,200)  # (width=650, height=350, startx=200, starty=200)
t.pu()
t.goto(-250,0)
t.pd()
t.pensize(20)
t.pencolor("pink")
t.seth(-40)
for i in range(4):
            t.circle(40,80) 
            #t.fd(20)
            t.circle(-40,80)
            #t.fd(20)
t.circle(40,40)
t.fd(10)
t.circle(20,180)
t.fd(20)
            

t.done()