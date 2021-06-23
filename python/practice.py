#practice.py
'''
num=3+5j
print(type(num))
print(num)
print('the real part', num.real)

a=pow(3,pow(3,99),100000000)
print(a)
'''

#'''
import turtle
i = int(input('你想要几边来密封呢？'))
angle = 360.0 / i
distance = 1000.0 / i
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(distance,steps=i)
turtle.end_fill()
turtle.done()