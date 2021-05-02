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
'''
import time
#import io
#dummy_file = io.StringIO()
scale=50            #可以任意定义
print("start processing".center(scale,"-"))         #.center() function
start = time.perf_counter()             #cpu start time counting
for i in range(scale+1):
    a = (i/scale)*100
    #print(a)
    b = '█' * i
    c = '.' * (scale-i)
    dur=time.perf_counter()-start           #time consumption of every percent counting
    print("\rStarting:"+"[{}-{:^4.0f}%->{}] {:.1f}s".format(b,a,c,dur),end='',flush = True)
    #print("\rStarting:"+"[{}-{:^4.0f}%->{}] {:.1f}s".format(b,a,c,dur),end='',file=dummy_file)           #槽位，end=''同行结束后不换行并带字符''，\r光标回到此行头部
    time.sleep(0.05)
print(" Done!")
#dummy_file.getvalue()
#print("\n"+"end processing".center(scale,'-'))          #two prints can be combined into one prints by using "+"
'''
'''
ew = eval(input("the weight on earth:"))
year = eval(input("the years you experienced:"))
print("the weight you input:{}".format(ew))
ew = ew + 0.5*year
mw = ew*0.165
print("in {} years your weight on earth would be:{}".format(year,ew))
print("Your weight on the moon in {} years will be {:.2f}".format(year,mw))
'''

'''
day_start = 1
day_up = 0.01
for i in range(365):
    if i % 11 in range(4,8):
        day_start = day_start *(1+0.01)
    else:
        day_start = day_start * 1
print("the day day up after 365: {:.2f}".format(day_start))
'''
'''
text1 = input("please input a 5 characters text:")
text2 = text1[::-1]
if len(text1) == 5:
    if text1 == text2:
        print("The text you input was 回文")
    else:
        print("the text you input was not 回文")
else:
    print("your input is not correct")
'''
'''
for i in range(11):
    if i % 5 in [0]:
        print("+"+"+".center(21,"-")+"+")
        #print(("{:11}").format("+ - - - - + - - - -  +"))
    else:
        print("|"+"|".center(21," ")+"|")
'''
from tqdm import tqdm
from time import sleep

for i in tqdm(range(100)):
    sleep(0.1)