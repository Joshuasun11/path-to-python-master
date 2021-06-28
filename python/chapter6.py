#chapter6.py
'''
s = "python123.io"
print(max(s))
print(min(s))
'''
'''
ls1 = ['x',20,1,10]
ls2 = ['y',10,5,122]
if ls1>ls2: #比较比的是第一个元素的大小
    print('true')
else:
    print('false')

'''
def Numinput(): #loop of getting input from a user
    '''
    nums = []
    iNumStr =input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    nums = []
    nums = list(input("Please input numbers: ").split())
    '''
    s = input("PLease input numbers split with ',' : ")
    nums = list(eval(s))
    return nums
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
        return s/len(numbers)
    
def dev(numbers, mean): #方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev+(num - mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = Numinput()
m = mean(n)
print("平均值：{}，方差：{:.2},中位数：{}.".format(m,dev(n,m),median(n)))