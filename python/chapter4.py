
'''
try:
    num =eval(input("please input a number:"))
    print(num**2)
except:
    print("输入的no good, not a number")
'''
'''
#CalBMIv3.py
height,weight = eval(input("Please input your weight and height,seperated by comma:"))
bmi = weight / pow(height,2)
print("your height:{:.2f} ,weight{:.2f} ".format(height,weight))
print("Your BMI:{:.2f}".format(bmi))
who,nat = "",""
if bmi < 18.5:
    who,nat = "偏瘦","偏瘦"
elif 18.5 <= bmi < 24:
    who,nat = "正常","正常"
elif 24 <= bmi < 25:
    who,nat = "正常","偏胖"
elif 25 <= bmi < 28:
    who,nat = "偏胖","偏胖" 
elif 28 <= bmi < 30:
    who,nat = "偏胖","肥胖" 
else:
    who,nat = "肥胖","肥胖"
print("BMI指标为：国际'{0}',国内'{0}'".format(who,nat))
'''

'''
s = "hello"
while s != "":
    for c in s: #repeat every characters of hello from here
        print("\nchecking {0}, and remaining: ".format(c)+s)
        if c == "l":
            #continue
            break
        print("\n"+c, end="")
    #s = s[:-1]
    s1 = s[-1]
    s = s[:-1]
    #print("\n*****one full loop, the {0} been deleted and remaining:".format(c)+s+"*****") #for continue loop
    print("\n*****one full loop, the '{0}' been deleted and remaining: '{1}'".format(s1,s)+"*****")  #for 'break' loop, once the 'if' detect the first l
                                                                                            #the for loop finished. the c would be "l"
    
'''
import random
random.seed(10)
print(random.random())