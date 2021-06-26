'''
Happy Birthday Isabella
'''
import turtle as t
import time

#sky
t.speed(7)
t.pu()
t.goto(-800,0)
t.pd()
t.pensize(800)
t.color('lightskyblue1')
t.fd(1500)

#earth
t.speed(5)
t.pu()
t.goto(-500,-260)
#t.right(10)
t.pd()
t.pensize(150)
t.color("green")
t.fd(1000)

#画佩奇
t.pensize(4)
t.hideturtle()
t.colormode(255)
t.color((255, 155, 192), "pink")
t.setup(1280, 800,)
t.speed(0)
# 鼻子
t.pu()
t.goto(-400, 80)
t.pd()
t.seth(-30)
t.begin_fill()
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
t.end_fill()
t.pu()
t.seth(90)
t.fd(25)
t.seth(0)
t.fd(10)
t.pd()
t.pencolor(255, 155, 192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160, 82, 45)
t.end_fill()
t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255, 155, 192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160, 82, 45)
t.end_fill()
# 头
t.color((255, 155, 192), "pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300, -30)
t.circle(100, -60)
t.circle(80, -100)
t.circle(150, -20)
t.circle(60, -95)
t.seth(161)
t.circle(-300, 15)
t.pu()
t.goto(-400, 80) #############
t.pd()
t.seth(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
t.end_fill()
# 耳朵
t.color((255, 155, 192), "pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50, 50)
t.circle(-10, 120)
t.circle(-50, 54)
t.end_fill()
t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50, 50)
t.circle(-10, 120)
t.circle(-50, 56)
t.end_fill()
# 眼睛
t.color((255, 155, 192), "white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")#
t.pu()
t.seth(90)#
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
t.color((255, 155, 192), "white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)#
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
# 腮
t.color((255, 155, 192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()
# 嘴
t.color(239, 69, 19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30, 40)
t.circle(40, 80)
# 身体
t.color("red", (255, 99, 71))
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-78)
t.pd()
t.begin_fill()
t.seth(-130)
t.circle(100, 10)
t.circle(300, 30)
t.seth(0)
t.fd(230)
t.seth(90)
t.circle(300, 30)
t.circle(100, 3)
t.color((255, 155, 192), (255, 100, 100))
t.seth(-135)
t.circle(-80, 63)
t.circle(-150, 24)
t.end_fill()
# 手
t.color((255, 155, 192))
t.pensize(10)
t.pu()
t.seth(90)
t.fd(-40)
t.seth(0)
t.fd(-27)
t.pd()
t.seth(-160)
t.circle(300, 15)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-10)
t.circle(-20, 90)
t.pu()
t.seth(90)
t.fd(30)
t.seth(0)
t.fd(237)
t.pd()
t.seth(-20)
t.circle(-300, 15)
t.pu()
t.seth(90)
t.fd(20)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-170)
t.circle(20, 90)
# 脚
t.pensize(10)
t.color((240, 128, 128))
t.pu()
t.seth(90)
t.fd(-75)
t.seth(0)
t.fd(-180)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
t.pensize(10)
t.color((240, 128, 128))
t.pu()
t.seth(90)
t.fd(40)
t.seth(0)
t.fd(90)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
# 尾巴
t.pensize(5)
t.color((255, 155, 192))
t.pu()
t.seth(90)
t.fd(70)
t.seth(0)
t.fd(95)
t.pd()
t.seth(0)
t.circle(70, 20)
t.circle(10, 330)
t.circle(70, 30)

#写字
#printer = t.Turtle()
#t.hideturtle() #多加了一个乌龟
t.pu()
t.goto(-100,-20)
t.color('red')
#t.fd(-50)
t.write("Isabella, Happy 1st Birthday!!",align="left",font=("Comic Sans MS",35,"bold"))
#t.exitonclick()
#t.reset()
t.home()

#花儿
def gt(x,y):
    t.pu()
    t.home()
    t.goto(x,y)
    
def flower(size,length,color):
    t.pu()
    #t.goto(300,-100)
    #画花枝干和叶子
    t.pd()
    t.left(90)
    t.pensize(5)
    t.color('lightgreen')
    t.fd(length/4)
    t.right(90)
    t.fd(5)
    t.bk(5)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(8)
    t.bk(8)
    t.right(90)
    t.fd(length/2)
    t.pu()
    
    #画花
    t.left(90)
    t.fd(size/4)
    t.right(180)
    t.pensize(1)
    t.begin_fill()
    t.color('red', color)
    t.pd()
    for i in range(10):
        t.fd(size)
        t.circle(10,200)
        #if abs(t.pos())<1:
            #break
        t.fd(size/2)
    t.end_fill()
    #t.done()
gt(200,-300)
flower(20,50,'mediumvioletred')#4
gt(300,-200)
flower(60,85,'darkorchid2')#5
gt(0,-230)
flower(30,60,'blue2')#1
gt(50,-280)
flower(40,65,'orange')#2
gt(150,-210)
flower(45,55,'limegreen')#3
gt(350,-250)
flower(35,70,'yellow')#6
gt(500,-280)
flower(50,90,'palevioletred1')#8
gt(440,-310)
flower(25,40,'cyan')#7

#烟花
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
fireworks(4,45,'seagreen2')
gt(350,100)
fireworks(8,22,'gold')

t.pu()
gt(420,-355)
t.color('white')
t.write("Dad-Josh Sun, 06/18/2021",align="left",font=("幼圆",10,"bold"))

t.exitonclick()