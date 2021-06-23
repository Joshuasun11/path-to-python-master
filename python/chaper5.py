#chaper5practice.py
'''
def test(n,*m):     #可变参数传递，*b可以自定义
    a = 0
    for i in range(n):
        a += 1
        print(a)
    for item in m:
        print(item)
    return a
    
test(5,'oh!','damn','shit','man')
'''
'''
y,n = 31,11
def func(n):
    #global y
    y=31
    for i in range(1,n+1):
        y += i
    return y
print(func(n),y)
'''

'''
def rvs(s):
    if s=="":
        return s
    else:
        return rvs(s[1:])+s[0]
          
l="12345"
#print(rvs(l))
l2=rvs(l)
print(l2)
print(l2[::-1])
'''
def test(x):
    return 0

