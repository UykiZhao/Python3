from random import *
# 生成列表写入1000个字母
a = list()
for i in range(1000):
    j = chr(randrange(97, 123))
    a.append(j)

# 生成字典并且进行字频统计
dict01 = {index: a.count(index) for index in a}
n = 0

for k in range(97, 123):
    # 生成24个字母
    m = chr(k)
    n += 1
    # 输出结果
    print(f'{m}:{dict01.get(m)}', end='  ')
    if n % 6 == 0:
        print()
