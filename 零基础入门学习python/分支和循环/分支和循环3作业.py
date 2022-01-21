"""
作者：Shuaiyu Li
日期：2022年01月15日
"""
"""抛硬币实验"""

import random

counts = int(input("请输入抛硬币的次数："))

if counts >= 100:
    ignore = True
else:
    ignore = False

top = 0
bottom = 0
i = 0

print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 2)

    if num % 2:
        top = top + 1
        if not ignore:
            print("正面", end=" ")

    else:
        bottom = bottom + 1
        if not ignore:
            print("反面", end=" ")

    i = i + 1

print("一共模拟了",counts,"次实验，结果如下：")
print("正面: ", top, "次", sep="")
print("反面: ", bottom, "次", sep="")