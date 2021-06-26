import turtle as t
# Turtle initialization
t.bgcolor("lightskyblue2") # background color
t.title("Fireworks")
t.speed(0)
def gt(x,y):
    t.pu()
    t.home()
    t.goto(x,y)
def fireworks(size,x,color):
    for x in range(x):
        step = 300/size

        if x % 2 == 0:
            t.color(color)
            step = 300/size
        elif x % 3 ==0:
            t.color("springgreen3")
            step = 250/size
        elif x % 5 == 0:
            t.color("yellow")
            step = 200/size
        else:
            t.color("hotpink")
            step = 180/size
        t.pd()
        t.forward(step)# Draw a straight line according to the step length
        t.dot(6)
        t.backward(step)# Return to the original way
        t.right(size*2)# Turn right # degrees each time
gt(0, 150)
fireworks(9,20,'rosybrown')
gt(200,200)
fireworks(5,40,'lightpink')
gt(-100,300)
fireworks(7,28,'whitesmoke')
gt(400,350)
fireworks(2,90,'dodgerblue2')
gt(100,310)
fireworks(4,45,'seagreen1')
gt(350,100)
fireworks(8,22,'gold')

t.pu()
gt(450,-350)
t.color('white')
t.write("Dad-Josh Sun, made in 06/2021",align="left",font=("幼圆",10,"bold"))
t.done()