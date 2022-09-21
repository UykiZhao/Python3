def trapeziumarea(x,y,h):       #x为上底，y为下底，h为高
    print(abs((x+y)*h/2))
x=int(input("请输入上底的长度："))
y=int(input("请输入下底的长度："))
h=int(input("请输入高的长度: "))
trapeziumarea(x,y,h)