"""
作者：Shuaiyu Li
日期：2022年01月14日
"""
print(6/2)
print(1.0+2.0)
print(3.14e5)

"""字符串和整数是不能相加的"""
age=18
print('祝小甲鱼',str(age),'岁生日快乐')  #加号没空格，逗号有空格

'''整数加法'''
import decimal
a=decimal.Decimal('0.1')
b=decimal.Decimal('0.1')
c=decimal.Decimal('0.1')
d=decimal.Decimal('0.3')
print(a+b+c-d)

"""抛硬币实验"""
# 导入随机模块 #
import random
# 接收用户输入并将数值赋值给 counts 变量 #
i = 0
counts=200
print("开始抛硬币实验：")
while i < counts:
    # 生成一个随机数num #
    num=random.randint(1,2)
    if num < 2:
        # 打印结果 #
        print('正面',end=" ")
    else:
        # 打印结果 #
         print('反面',end=" ")
    i = i + 1

"""抛硬币实验模板"""
import random

counts = int(input("请输入抛硬币的次数："))
i = 0

print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 10)

    if num % 2:
        print("正面")
    else:
        print("反面")

    i += 1

"""计算 1000000 以内所有偶数的和"""
i = 0
sum = 0
while i <= 1000000:
    if i % 2 == 0:
        sum=i+sum
    i = i + 1
print("1000000以内所有偶数的和为:",sum)

"""小麦问题"""
# 初始化变量 i #
# 初始化变量 sum #
i=0
sum=0
while i <= 64:
    # 请计算每一个格子的麦子数，并将其赋值给 wheats 变量#
    wheats=2**(i-1)
    sum = sum + wheats
    i = i + 1

print("舍罕王应该给达依尔", sum, "粒麦子！")
