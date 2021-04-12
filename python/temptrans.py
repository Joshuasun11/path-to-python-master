# temptrans.py
val = input("please input temperature: ")
#print(val[2])
if val[-1] in ['F','f']: 
   # C = (eval(val[0:-1])-32)/1.8
    print("转换后温度为: {:.2f}C".format((eval(val[0:-1])-32)/1.8)) #.format()
elif val[-1] in ['C', 'c']:
   # F = 1.8*eval(val[0:-1])+32
    print("转换后温度为: {:.2f}F".format(1.8*eval(val[0:-1])+32))
else:
    print("输入格式错误")