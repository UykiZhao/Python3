num1,num2,num3 =map(int,input('请输入三个数字：(空格隔开)').split())

Max = lambda num1,num2,num3:max(num1,num2,num3)

print('最大数是：',Max(num1, num2, num3))
