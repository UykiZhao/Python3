from turtle import *

c = ['Blue', 'Red', 'Gold', 'Green', 'Purple']
n = 0
for i in range(5):
    # 设置填充颜色
    fillcolor(c[i])
    begin_fill()
    # 转90度朝向y轴，再抬笔到画线处
    left(90)
    penup()
    # 从大圆画起，下笔
    j = 100-20*i
    forward(j)
    pendown()
    left(90)
    circle(j)
    end_fill()
    # 抬笔回到原点
    penup()
    home()
done()