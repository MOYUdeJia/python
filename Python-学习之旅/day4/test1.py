# 猜数字小游戏

import random

answer = random.randint(1,100)
counter = 0

while True:
    counter += 1
    number = int(input('请输入数字：'))
    if number > answer:
        print('小一点')
    elif number < answer:
        print('大一点')
    else:
        print('猜对了')
        break
print('您一共猜了%d次' % counter)