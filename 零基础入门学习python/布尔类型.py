"""
作者：Shuaiyu Li
日期：2022年01月14日
"""
year = input('请输入一个年份：')

while not year.isdigit():
    year = input("抱歉，您的输入有误，请输入一个整数：")

# 将 year 转换成整数 #
year=int(year)
if year % 400 == 0:
    print(year,'是世纪闰年！')
else:
    if year % 4 == 0 and year % 100 != 0:
        print(year,'是闰年！')
    else:
        print(year,'不是闰年')