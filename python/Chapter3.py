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
'''
import time
for i in range(101):
    print("\r{:3} %".format(i),end=" ")
    time.sleep(0.1)
'''
import time
scale=50            #可以任意定义
print("start processing".center(scale,"-"))         #.center() function
start = time.perf_counter()             #cpu start time counting
for i in range(scale+1):
    a = (i/scale)*100
    #print(a)
    b = '*' * i
    c = '.' * (scale-i)
    dur=time.perf_counter()-start           #time consumption of every percent counting
    print("\r [{}-{:^4.0f}%->{}] {:.1f}s".format(b,a,c,dur),end='')           #槽位，end=''同行结束后不换行并带字符''，\r光标回到此行头部
    time.sleep(0.1)
print("\n"+"end processing".center(scale,'-'))          #two prints can be combined into one prints by using "+"

