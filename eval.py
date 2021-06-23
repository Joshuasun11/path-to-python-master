#eval使用详解
#1.eval无参实现字符串转化

s = '1+2+3*5-2'
print(eval(s))  #16
 
#2.字符串中有变量也可以
x = 1
print(eval('x+2'))  #3
 
#3.字符串转字典
print(eval("{'name':'linux','age':18}"))
#输出结果：{'name':'linux','age':18}
 
#4.eval传递全局变量参数,注意字典里的:age中的age没有带引号，说明它是个变量，而不是字符串。
#这里两个参数都是全局的
print(eval("{'name':'linux','age':age}",{"age":1822}))
#输出结果：{'name': 'linux', 'age': 1822}
print(eval("{'name':'linux','age':age}",{"age":1822},{"age":1988})
#输出结果：{'name': 'linux', 'age': 1823}
 
#eval传递本地变量，既有global和local时，变量值先从local中查找。
age=18
print(eval("{'name':'linux','age':age}",{"age":1822},locals()))
#输出结果：{'name': 'linux', 'age': 18}
print("-----------------")
 
print(eval("{'name':'linux','age':age}"))

'''
eval是Python的一个内置函数，功能十分强大，这个函数的作用是，返回传入字符串的表达式的结果。就是说：将字符串当成有效的表达式 来求值 并 返回计算结果。

    eval函数就是实现list、dict、tuple与str之间的转化，同样str函数把list，dict，tuple转为为字符串

1.eval的语法
eval(expression[, globals[, locals]])
expression ： 表达式。
globals ： （可选参数)变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals ： (可选参数)变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
既然eval有两个可选参数是命名空间，那么先搞清楚啥是命名空间吧？

2.命名空间
【定义】

    名称到对象的映射。python是用命名空间来记录变量的轨迹的，命名空间是一个dictionary，键是变量名，值是变量值。各个命名空间是独立没有关系的，一个命名空间中不能有重名，但是不同的命名空间可以重名而没有任何影响。

【分类】

    python程序执行期间会有2个或3个活动的命名空间（函数调用时有3个，函数调用结束后2个）。按照变量定义的位置，可以划分为以下3类：

    Local，局部命名空间，每个函数所拥有的命名空间，记录了函数中定义的所有变量，包括函数的入参、内部定义的局部变量。

    Global，全局命名空间，每个模块加载执行时创建的，记录了模块中定义的变量，包括模块中定义的函数、类、其他导入的模块、模块级的变量与常量。

    Built-in，python自带的内建命名空间，任何模块均可以访问，放着内置的函数和异常。

【生命周期】

    Local（局部命名空间）在函数被调用时才被创建，但函数返回结果或抛出异常时被删除。（每一个递归函数都拥有自己的命名空间）。

    Global（全局命名空间）在模块被加载时创建，通常一直保留直到python解释器退出。

    Built-in（内建命名空间）在python解释器启动时创建，一直保留直到解释器退出。

    各命名空间创建顺序：python解释器启动 ->创建内建命名空间 -> 加载模块 -> 创建全局命名空间 ->函数被调用 ->创建局部命名空间

    各命名空间销毁顺序：函数调用结束 -> 销毁函数对应的局部命名空间 -> python虚拟机（解释器）退出 ->销毁全局命名空间 ->销毁内建命名空间

    python解释器加载阶段会创建出内建命名空间、模块的全局命名空间，局部命名空间是在运行阶段函数被调用时动态创建出来的，函数调用结束动态的销毁的。

   python的全局命名空间存储在一个叫globals()的dict对象中；局部命名空间存储在一个叫locals()的dict对象中。可以用print (locals())来查看该函数体内的所有变量名和变量值。

print(locals())  #打印显示所有的局部变量

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001B22E13B128>,
'__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/pythoyworkspace/file_demo/Class_Demo/pachong/urllib_Request1.py',
'__cached__': None, 's': '1+2+3*5-2', 'x': 1, 'age': 18}
Process finished with exit code 0
'''

eval的使用与风险
python3中input将接受的结果存为字符串，一般来说，可以使用eval实现表达式的还原，并且实现表达式的计算，比如下面使用eval直接完成了表达式的还原与计算：

>>> s = input("输入一个表达式")
输入一个表达式：1+3+4+4*3
>>> print(eval(s))
20
>>>
eval虽然方便，但是要注意安全性，可以将字符串转成表达式并执行，就可以利用执行系统命令，删除文件等操作。，比如用户恶意输入就会获得当前目录文件

>>>eval("__import__('os').system('dir')")
 驱动器 C 中的卷是 OS
 卷的序列号是 B234-8A38
 
 C:\Users\Robot_TENG 的目录
 
2019-07-01  09:11    <DIR>          .
2019-07-01  09:11    <DIR>          ..
2017-11-23  16:15    <DIR>          .android
2018-12-23  00:02    <DIR>          .conda
2018-12-06  19:08                20 .dbshell
2017-12-01  19:28    <DIR>          .eclipse
2018-01-22  22:46    <DIR>          .idea-build
2017-12-31  14:49    <DIR>          .IdeaIC2017.1
2018-01-22  21:21    <DIR>          .IdeaIC2017.2
2019-07-01  09:11    <DIR>          .ipynb_checkpoints
2018-12-19  20:04    <DIR>          .ipython
2019-07-01  09:30    <DIR>          .jupyter
2017-12-01  16:11    <DIR>          .m2
2017-12-31  23:14                 0 .mongorc.js
2019-02-03  22:52    <DIR>          .p2
2018-07-16  22:04    <DIR>          .PyCharm2016.1
2018-12-06  19:49    <DIR>          .rdm
2018-01-22  22:09               580 .scala_history
2018-12-06  19:19    <DIR>          .vscode
2019-06-21  16:37    <DIR>          3D Objects
2019-06-21  16:37    <DIR>          Contacts
2019-07-01  16:21    <DIR>          Desktop
2019-06-28  16:34    <DIR>          Documents
2019-06-28  10:26    <DIR>          Downloads
2018-09-11  22:24    <DIR>          Evernote
2019-06-21  16:37    <DIR>          Favorites
2018-08-02  23:58    <DIR>          HBuilder
2018-08-03  00:00    <DIR>          HBuilder settings
2018-08-03  00:02    <DIR>          HBuilderProjects
2019-06-21  16:37    <DIR>          Links
2019-06-21  16:37    <DIR>          Music
2018-03-18  00:22    <DIR>          Oracle
2019-06-21  16:37    <DIR>          Pictures
2019-06-21  16:37    <DIR>          Saved Games
2019-06-21  16:37    <DIR>          Searches
2018-12-23  00:47               690 Untitled.ipynb
2019-07-01  09:11                72 Untitled1.ipynb
2019-06-30  18:43    <DIR>          Videos
2019-01-13  18:20    <DIR>          Yinxiang Biji
               5 个文件          1,362 字节
              34 个目录 72,365,862,912 可用字节
————————————————
版权声明：本文为CSDN博主「涤生手记」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_26442553/article/details/94396532
'''
