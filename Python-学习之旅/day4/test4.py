# 打印三角形图案
row = int(input('请输入行数：'))

for i in range(row):
    for j in range(i+1):
        print('*', end='')
    print()

# 根据从左到右输出的原则，面对前面是空格的形式，考虑先输出空格！！！
# 嵌套循环，i表示第i行，j表示第j列！！！
for i in range(row):
    for j in range(row):
        if j < row-i-1:
            print(' ', end='')
        else:
            print('*', end ='')
    # 前面的循环不包含换行，因此每循环完一行要单独换行。
    print()

# 由上次循环得出大致总体框架：先行，后列，最后换行
# 由于i的每一次循环表示的是一行，因此可以把这一行分两次print，第一次print左边空格，第二次print中间五角，右边空格不需要print，中间不要换行。
for i in range(row):
    for j in range(row-i-1):
        print(' ', end ='')
    for j in range(2*(i+1)-1):
        print('*', end ='')
    print()


# 小结：对于图形的输出要遵循从左到右输出的规律，思考从左到右依次是什么。