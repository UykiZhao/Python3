a={1,2,3,4,5}
b={4,5,6,7,8}
#求差集
print("a与b的差集为：",a-b)
#求并集
print("a与b的并集为：",a|b)
#求交集
print("a与b的交集为：",a&b)
#判断集合是否在a或b里面
x=int(input("输入一个数字："))
if x in a and x not in b:
    print("%d在集合a里面！"%x)
elif x in b and x not in a:
    print("%d在集合b里面！"%x)
elif x in a and x in b:
    print("%d在集合a和b里面！" %x)
else:
    print("%d不在集合a和b里面！"%x)