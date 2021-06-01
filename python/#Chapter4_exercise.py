#Chapter4_exercise.py
'''
k=10000
i = 0
while k>1:
    print(k)
    i+=1
    
    k=k/2
print(i)
'''
'''
i = 4321
print(i)
t = str(i)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
'''

#s = '1+2+3*5-2'
#print(eval(s))
#print(s)
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4) + pow(eval(t[3]),4) == i :
        print(i)