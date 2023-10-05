year = int(input('请输入年份p判断是否是闰年：'))

x = year % 4 == 0 and year % 100 != 0
print(x)
