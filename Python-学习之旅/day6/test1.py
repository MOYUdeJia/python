# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gcd(x,y):
    if x<y:
        x,y=y,x
    for i in range(y,0,-1):
        if y % i == 0 and x % i ==0:
            return i

def gbs(x,y):
    return(x*y//gcd(x,y))

print(gcd(8,12))
print(gbs(8,12))