"""
作者：Shuaiyu Li
日期：2022年01月15日
"""
"""每日检查"""
day = 1
while day <= 7:
    answer = input("今天有好好学习吗")
    if answer != "有":
        break
    day += 1
else:
    print("非常棒，你已经坚持了七天了")
###  while—else循环语句可以检查是否跳出循环，while-else 可以非常容易地检测到循环的退出情况

"""循环结构的嵌套"""
i = 1
while i <= 9 :
    j = 1
    while j <= i :
        print(j, "*", i, "=", j*i, end=" ")
        j += 1
    print()
    i += 1

"""break 和 continue"""
