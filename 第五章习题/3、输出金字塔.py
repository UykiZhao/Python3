m=9
for i in range(m):
    for j in range(m-i-1):
        print(' ',end='')
    for l in range(i):
        print(chr(ord('A')+i-l),end='')
    for k in range(i+1):
        print(chr(ord('A')+k),end='')
    print('')