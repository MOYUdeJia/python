# 在屏幕上显示跑马灯文字。
import os
import time

def main():
    content = '海口是个美丽的城市，欢迎来到海口！'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content=content[1:]+content[0] # 每次循环把字符串content序号0位置处的字符放到最后，实现跑马灯的效果。


if __name__ == '__main__':
    main()