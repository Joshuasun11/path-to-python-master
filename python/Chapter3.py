'''
import time
t = time.localtime()
time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(time.strftime("%Y-%m-%d  %H:%M:%S",t))
print(time.strftime("%D %H:%M:%S"))
print(time.strftime("%Y-%B-%d  %H:%M:%S",t))
'''
'''
#TextProBarV1.py
import time
scale = 10
print("------start processing------")
for i in range(scale+1): #scale = 10 but it starts counting from 0
    a = '*' * i
    b = '.' *(scale-i)   
    c = (i/scale)*100
    print("{:>4.0f} %[{}->{}]".format(c,a,b))  #>4 右对齐加4个宽度，可以尝试1，2个宽度看效果
    time.sleep(0.1)
print("------end processing------")
'''
import time
for i in range(101):
    print("\r{:3} %".format(i),end=" ")
    time.sleep(0.1)