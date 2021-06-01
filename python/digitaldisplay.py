#digitaldisplay.py
'''
using turtle to draw digital style numbers
gain a series of numbers then display them by turtle
gain the system time, then display them by the turtle
'''
import time
from datetime import date
import turtle as t

def drawline(draw): #draw a line
    t.pu()
    t.fd(5)
    t.pd() if draw else t.pu()
    '''
    if draw:
        t.pd()
    else: 
        t.pu()
       ''' 
    t.fd(40)
    t.pu()
    t.fd(5)
    t.right(90)
def drawdigit(digit): #draw a digit
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    t.left(180)
    t.pu()
    t.fd(20)
    
def drawdate(date):
    for i in date:
        drawdigit(eval(i))
def main():
    t.setup(850,450,200,200)
    t.pu()
    t.fd(-400)
    t.pensize(6)
    t.speed(0)
    #drawdate('20210517')
    #t.done()
    c = date.today().strftime('%Y-%m-%d')
    #t1 = time.asctime(c)
    print(c)
    
    ###########print time by turtle#############
    #printer = t.Turtle()
    #printer.hideturtle() #多加了一个乌龟
    c = date.today().strftime('%Y')
    drawdate(c)
    t.write("年", True,font=("楷体", 35, "bold"))
    t.fd(30)
    
    c = date.today().strftime('%m')
    drawdate(c)
    t.write("月", True,font=("楷体", 35, "bold"))
    t.fd(30)
    
    c = date.today().strftime('%d')
    drawdate(c)
    t.write("日",True, font=("楷体", 35, "bold"))
    
    t.done()
main()

#onlineVersion
'''
import turtle as t
import datetime
def drawGap(): #绘制数码管间隔
    t.penup()
    t.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    t.pencolor("red")
    for i in date:
        if i == '-':
            t.write('年', font=("Arial", 18, "normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == '=':
            t.write('月', font=("Arial", 18, "normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == '+':  
            t.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    t.setup(800, 350, 200, 200)
    t.speed(0)
    t.penup()
    t.fd(-350)
    t.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    t.hideturtle()
    t.exitonclick()
main()
'''

     
