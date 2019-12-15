# 圆周率的计算
# 近似计算公式：
#
# pai = {[1/(16的k次幂) * (4/(8*k+1)) - (2/(8*k+4)) -(1/(8*k+5)) - (1/(8*k+6)))]}的和
#       k = 0 到 无穷 
#
#  蒙特卡罗方法：随机撒点
#
#方法2：蒙特卡罗方法
#单位正方形

# CalPiV2.py
from random import random
from time import perf_counter
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS + 1):
    x, y = random(), random()
    dist = pow(pow(x,2) + pow(y,2), 0.5)  # 点到圆心的距离
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/DARTS)
print('圆周率值是：{}'.format(pi))
print('运行时间是：{:.5f}s'.format(perf_counter() - start))