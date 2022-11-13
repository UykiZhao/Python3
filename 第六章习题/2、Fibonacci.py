def fibonacci(n):
    fn=list()
    if n==1:
        fn.append(0)
        print(fn)
    elif n==2:
        fn.append(0)
        fn.append(1)
        print(fn)
    else:
        fn.append(0)
        fn.append(1)
        for i in range(2,n):
            fn.append(fn[i-2]+fn[i-1])
        else:
            print(fn)

n = int(input('请输入斐波那契数列前几项：'))
fibonacci(n)