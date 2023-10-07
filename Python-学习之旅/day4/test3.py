# test3：输入两个正整数，计算它们的最大公约数和最小公倍数。
# 两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
x = int(input('x='))
y = int(input('y='))
# 让y成为那个较大的数
if x>y:
    x,y = y,x
# 从两个数中较小的数开始递减，例如8，12
# 最大公约（因）数：4（从较小的那个数往下找）
# 最小公倍数：24（从较大的那个数往上找）
# a*b=最大公约数*最小公倍数
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x,y,factor))
        print('%d和%d的最大公约数是%d' % (x,y,x*y/factor))
        break






