a=[]
c=int(input("请输入列表奇数个数："))

while True:
    b=int(input("请输入二十以内的奇数："))
    if b%2!=0 and b<20:
        a.append(b)
        if len(a)==c:
            break
    else:
        print("请重新输入！")
print(sum(a))