from math import pi
def ringarea(x,y):      #大圆半径为x,小圆半径为y
        print(pi*x*x-pi*y*y)
x=int(input("请输入大圆半径："))
y=int(input("请输入小圆半径："))
while True:
    if x<y or x==y:
        print("半径输入有误,请重新输入")
        x = int(input("请输入大圆半径："))
        y = int(input("请输入小圆半径："))
    else:
        ringarea(x,y)
        break