from turtle import *

color('purple', 'orange')
begin_fill()

# 抬笔走到一个端点在转角度
penup()
forward(100)
left(120)

# 落笔画第一条边
pendown()
forward(100)

# 循环画边
for i in range(5):
    left(60)
    forward(100)
end_fill()
done()
