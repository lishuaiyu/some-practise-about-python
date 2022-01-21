"""
作者：Shuaiyu Li
日期：2022年01月13日
"""
import random

"""双色球"""
red=random.sample(range(1,34),k=6)
blue=random.randint(1,16)
print('开奖结果是：',*red)
print("特别号码是：",blue)