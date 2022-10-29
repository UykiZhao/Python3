def primenumber(x):
   y=x+1
   while(True):
        for i in range(2,y):
            if y%i==0:
                y+=1
                break
        else:
            print('大于%d的最小素数是%d'%(x,y))
            break
x=int(input('请输入一个正整数:'))
primenumber(x)