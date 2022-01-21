"""
作者：Shuaiyu Li
日期：2022年01月14日
"""
love = 'yes'
while love == 'yes':
    love = input("今天你还爱我吗：")

i = 1
sum = 0
while i < 10:
    sum = sum + i
    i = i + 1
print(sum)

"""口号"""
while True:
    a=input('请输入一句口号（输入STOP结束）：')
    if a == 'STOP' :
        break
    print(a)

"""抛硬币实验"""

import random

counts = int(input("请输入抛硬币的次数："))
top=0
bottom=0
i = 0

print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 2)

    if num % 2:
        print("正面", end=" ")
        top = top + 1
    else:
        print("反面", end=" ")
        bottom = bottom - 1
    i = i + 1

print("一共模拟了",counts,"次实验，结果如下：")
print("正面: ",top,"次",sep="")
print("正面: ",top,"次",sep="")