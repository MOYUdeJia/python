# 计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    if year % 4 ==0 and year % 100 !=0 or year % 400 ==0:
        return True
    else:
        return False
# 给定三个时间，判断这是一年的第几天。
# 通过year得到是闰年还是平年，通过month利用循环计算出前面的月总共有多少天，最后通过加上date即可算出第几天。
def which_day(year,month,date):
    day_of_month=[
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += day_of_month[index]
    return total+date

def main():
    print(which_day(1945,10,1))
    print(which_day(1990,1,20))
    print(which_day(1971,5,28))
    print(which_day(1997,12,23))
    print(which_day(2003,2,12))
    print(which_day(2023,10,14))

if __name__ == '__main__':
    main()
