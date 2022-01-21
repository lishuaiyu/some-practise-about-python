"""
作者：Shuaiyu Li
日期：2022年01月15日
"""
i = 1
while i <= 9:
    j = 9
    while j >= i:
        print(j, "*", i, "=", j * i, end=' ')
        j -= 1
        print()
    i += 1