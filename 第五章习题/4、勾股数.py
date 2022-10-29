cnt=0
for i in range(1,51):
    for j in range(i,51):
        for k in range(j,51):
            if(i**2+j**2==k**2 or i**2+k**2==j**2 or j**2+k**2 == i**2):
                print('%2d'%i,'%2d'%j,'%2d'%k,sep=',',end='\t')
                cnt+=1
                if(cnt==6):
                    print()
                    cnt=0