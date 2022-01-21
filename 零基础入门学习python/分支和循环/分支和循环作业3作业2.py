"""
作者：Shuaiyu Li
日期：2022年01月15日
"""
import random

counts = int(input("请输入抛硬币的次数："))

if counts >= 100:
    ignore = True
else:
    ignore = False

top = 0
bottom = 0
i = 0

last = 0  # 记录上一次的状态，如果是正面设置为1, 反面则设置为2
c_top = 0  # 统计连续正面的次数
c_bottom = 0  # 统计连续反面的次数
max_top = 0  # 统计连续正面的最多次数
max_bottoms = 0  # 统计连续反面的最多次数


print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 2)

    if num % 2:
        top = top + 1
        if last == 1:
            c_top += 1
        else:
            c_top = 1
        if c_top > max_top:
            max_top=c_top

        if not ignore:
            print("正面", end=" ")
        last = 1

    else:
        bottom = bottom + 1
        if last == 2:
            c_bottom += 1
        else:
            c_bottom = 1
        if c_bottom > max_bottoms:
            max_bottoms=c_bottom

        if not ignore:
            print("反面", end=" ")
        last = 2
    i = i + 1

print("一共模拟了",counts,"次实验，结果如下：")
print("正面: ", top, "次", sep="")
print("反面: ", bottom, "次", sep="")
print('最多连续正面：',max_top)
print('最多连续反面：',max_bottoms)