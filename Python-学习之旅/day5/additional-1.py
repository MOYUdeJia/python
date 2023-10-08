# 生成斐波那契数列的前20个数。
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
x = 0
y = 1
z = 0
for i in range(0,20):
    z = x
    x = x + y  # 表示前面两个数的和
    y = z
    print(x)
# 每一次循环设计的范围是三个数，数列的第n个数x表示为前两项的和，第n-1个数是上次循环的x，第n-2个数是y，而y的值为上次循环刚开始时的x，因此，在一次循环开始时要记录此时x的值保存在z中并在循环结束时把z的值赋给y，以便下次循环使用。


   # 1   2   3   4  5
    #y   x   x
