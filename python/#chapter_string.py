#chapter_string.py
weekID="星期一星期二星期三星期四星期五星期六星期天"
dayinput=eval(input("please input number:"))
pos=(dayinput-1)*3
print(pos)
print(weekID[pos:(pos+3)]) #tempstr[a:b] the start position is a the ending position is b-1