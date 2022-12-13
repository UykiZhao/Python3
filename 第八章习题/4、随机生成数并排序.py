from random import *

# 生成列表
m = list()
for i in range(10):
    m.append(randrange(1000))

# 冒泡排序
for j in range(10):
    for k in range(9 - j):
        if m[k] > m[k + 1]:
            m[k], m[k + 1] = m[k + 1], m[k]
print(m)
