# 练习3：实现判断一个数是不是素数的函数。
def fun(x):
    if x==2:
        return True
    for i in range(2,x):
        if x % i == 0:
            return False
        if i == x-1:
            return True
if __name__ == '__main__':
    while True:
        y=int(input('x='))
        print(fun(y))