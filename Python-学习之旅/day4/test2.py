# test2：输入一个正整数判断是不是素数

number = int(input('请输入大于1的整数：'))
counter = 0

if number == 2:
    print('是素数')
else:
    for x in range(2,number):
        if number % x == 0:
            counter += 1
            break
    if counter ==0:
        print('是素数')
    else:
        print('不是素数')

# 小结：能不嵌套就不嵌套，看看能否用循环外的分支做出来。
# 判断是不是素数只需要遍历2到这个数的平方根就可以了。