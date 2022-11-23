l = [[]]
# 第一行添加1到5
for n in range(1, 6):
    l[0].append(n)
# 创建4个空列表
for n in range(1, 5):
    l.append([])
    # 往下添加数据
    for i in range(1, 5):
        l[n].append(l[n - 1][i])
    # 末尾补数据
    l[n].append(l[n - 1][0])
# 输出矩阵
for i in range(0, 5):
    for j in range(0, 5):
        print(l[i][j], end='  ')
    print()

# 写入矩阵
with open('矩阵.csv', 'w') as fp:
    for i in range(0, 5):
        for j in range(0, 5):
            print(l[i][j], end=' ', file=fp)
        print(file=fp)
