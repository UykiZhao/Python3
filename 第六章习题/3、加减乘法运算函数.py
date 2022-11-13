def add(num1,num2):
    print(f"{num1}+{num2}={num1+num2}")

def reduce(num1,num2):
    print(f"{num1}-{num2}={num1-num2}")

def multiplication(num1,num2):
    print(f"{num1}×{num2}={num1*num2}")

num1,num2 = map(int,input("请输入两个数:(空格隔开)").split())
add(num1, num2)
reduce(num1, num2)
multiplication(num1, num2)