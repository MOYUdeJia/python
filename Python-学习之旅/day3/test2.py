# 百分制成绩转换为等级制成绩
score = float(input('请输入分数：'))

if score>=90:
    grade = 'A'
elif score>=80:
    grade ='B'
elif score>=70:
    grade ="C"
elif score>=60:
    grade ="D"
else:
    grade ='E'
print('您的等级是：',grade)
