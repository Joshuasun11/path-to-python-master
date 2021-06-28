#calPI.py
'''
#from internet
import random
import numpy as np
def monte_carlo(total_points):
    """ 圆中点的个数除以总点数即为圆周率
    Args:
         total_points: 生成点总个数
    Returns:
         pi,以list形式返回所有的x和y点
    """
    # 1：定义圆中点个数的计数器与点容器
    num_circle_points = 0
    x_list = []
    y_list = []

    # 2：生成total_points个随机点
    for _ in range(total_points):
        # 3：在长宽均为1的矩形内生成随机点（x，y）
        rand_x = np.random.uniform(0, 1, size=1)
        rand_y = np.random.uniform(0, 1, size=1)
        x_list.append(rand_x)
        y_list.append(rand_y)
        # 4：判断随机点是否在圆内，如果在则圆中点个数计数器加1
        if np.add(rand_x ** 2, rand_y ** 2) <= 1:
            num_circle_points += 1

    # 5：根据圆中点个数与总点数的比值，即得到圆周率
    pi = 4 * float(num_circle_points) / float(total_points)
    
    return pi, x_list, y_list
    print(pi)
'''
'''
#online version 2
# Initilize denominator
k = 1
  
# Initilize sum
s = 0
  
for i in range(1000000):
  
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
  
        # odd index elements are negative
        s -= 4/k
  
    # denominator is odd
    k += 2
      
print(s)
'''
from random import random
from time import perf_counter
DARTS = 1000*1000 #the darts gonna be spread in specific area
bingo = 0 #init the value hits, which is the darts that hitted indside the num_circle_points
start = perf_counter()
for i in range(1,DARTS+1):
     x,y = random(),random()#spread the darts
     dist = pow(x**2+y**2,0.5)#calculate if the darts hitted inside the circle
     if dist <= 1.0:
          bingo = bingo + 1
     pi = 4 * (bingo/DARTS)
print("The pi is: {:<10f}".format(pi))
print("\nTime consumed: {0:.5f}".format(perf_counter()-start))