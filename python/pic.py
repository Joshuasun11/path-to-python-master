
import math
import turtle as t
import time
#草地
t.speed(0)
t.pu()
t.goto(-500,-260)
#t.right(10)
t.pd()
t.pensize(150)
t.color("green")
t.fd(1000)

#花儿
def gt(x,y):
    t.pu()
    t.home()
    t.goto(x,y)
    
def flower(size,length,color):#(flower size,枝干长度，画色)
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
flower(20,50,'white')#4
gt(300,-200)
flower(60,85,'white')#5
gt(0,-230)
flower(30,60,'white')#1
gt(50,-280)
flower(40,65,'gold')#2
gt(150,-210)
flower(45,55,'cyan')#3
gt(350,-250)
flower(35,70,'white')#6
gt(500,-280)
flower(50,90,'white')#8
gt(440,-310)
flower(25,40,'white')#7

'''
#烟火
t.pu()
t.home()
t.goto(300,300)
'''


t.exitonclick()
