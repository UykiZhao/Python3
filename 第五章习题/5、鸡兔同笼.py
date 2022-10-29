foot=80  #鸡为x 兔为y
for x in range(1,41):
    for y in range(1,21):
        if x*2+y*4==80:
            print("鸡有%2d只，兔有%2d只"%(x,y))