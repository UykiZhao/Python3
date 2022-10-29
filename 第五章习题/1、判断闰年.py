def Judgeleapyears(x):
    if (x%4==0 and x%100 != 0)or x%400==0:
        print('%d是闰年!\n'%x)
    else:
        print('%d不是闰年！\n'%x)
x=int(input('请输入一个年份:'))
Judgeleapyears(x)