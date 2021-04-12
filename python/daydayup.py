#daydayup.py
'''
dayup=1.00
d=0
w=0
dayfactor=0.01
for i in range(365):
    if i % 7 in [6,0]:
'''
'''
#method 1:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)
print("daydayup result: {:.2f}".format(dayup))
'''
'''
#method 2:
        d=d+1
    else:
        w=w+1
print("the weekends and weekdays are:", d,w)

dayup = pow((1-dayfactor),d)*pow((1+dayfactor),w)
print("total daydayup {:.2f} ".format(dayup)) s

'''

#daydayupPRO.py
def dayup(df): #def 用于设置函数 df是占位符
    dayup=1  
    for i in range(365):    
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup  #return 用于函数体内
dayfactor = 0.001
while dayup(dayfactor) < 37.78:
    dayfactor = dayfactor + 0.001

dayfactor*=100
print("weekdays needed power: {:.3f}%".format(dayfactor))
print("the power is: ",dayfactor)
