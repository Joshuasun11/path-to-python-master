#wordcountV1.py
'''
tempstr = ['p','y','t','h','o','n']
ts = tempstr[::-1]
print(ts)
'''
'''
def gettxt():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()       #将所有字符小写化
    for ch in '~!@#$%^&*()_-+=.}{|";/?,][:\\"':
        txt = txt.replace(ch," ")
    return txt

hamlettxt = gettxt()
words = hamlettxt.split() #将获取的文本转换为列表赋予word
counts = {}      #用字典类型数据结构来记录每个单词和其次数
for word in words:
    counts[word] = counts.get(word,0)+1 #向字典里添加字

#将字典里的键值对转换为列表
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) #由大到小的排序
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
    
'''
import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","主公","军士","左右","军马","引兵","次日","大喜","天下"
            ,"东吴","于是","今日","不敢","魏兵","陛下","一人"}
words = jieba.lcut(txt)   #精确词频统计
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    elif word == "都督" or word == "公瑾":
        rword = "周瑜"
    else:
        rword = word
    counts[rword]=counts.get(rword,0)+1
    
for word in excludes:
    del counts[word]
    
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
