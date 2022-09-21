x=[]
while True:
    a=int(input("请输入5个数："))
    x.append(a)
    if len(x)>4:
        break
x.sort()  #从大到小排序
print("从小到大排序为：",x)
x.sort(reverse=True)
print("从大到小排序为：",x)
