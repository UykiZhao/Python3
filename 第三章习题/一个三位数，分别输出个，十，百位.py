def eachbit(x):
    print("个位数为:",x%100%10)
    print("十位数为：",x%100//10)
    print("百位数为：",x//100)
x=int(input("输入一个三位数："))
eachbit(x)
