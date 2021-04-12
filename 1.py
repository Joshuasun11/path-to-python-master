'''
eval('print("Hello.. World!")')
'''

n = eval(input())
if n == 0:
    print("Hello World")
elif n > 0:
    print("He\nll\no \nWo\nrl\nd")
else:
    for w in "really":  #for 循环，w字符串一次读取一个字符并输出，默认纵向输出
        print(w)