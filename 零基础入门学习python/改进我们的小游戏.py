"""
作者：Shuaiyu Li
日期：2022年01月13日
"""
'''用Python设计第一个游戏'''

temp=input('不妨猜猜小甲鱼心里想的是什么')
guess=int(temp)

if guess ==8:
    print("你是小甲鱼心里的蛔虫吗")
    print('哼，猜中了也没有奖励')
else:
    if guess <8:
        print("小啦")
    else:
        print('大啦')

print('game over')


counts=3
while counts>0:
    print("i love you")
    counts=counts-1

'''用Python改进第一个游戏'''

counts=3
while counts >0 :
    temp=input('不妨猜猜小甲鱼心里想的是什么')
    guess=int(temp)

    if guess == 8:
        print("你是小甲鱼心里的蛔虫吗")
        print('哼，猜中了也没有奖励')
        break
    else:
        if guess < 8:
            print("小啦")
        else:
            print('大啦')
    counts=counts-1

print('game over')

"""成绩评级程序"""
grade=int(input("请输入你的分数："))
if grade < 60:
    print("D")
elif 60 <= grade < 80:
    print("C")
elif 80 <= grade < 90:
    print("B")
elif 90 <= grade < 100:
    print("A")
else:
    print("S")

"""成绩评级程序升级"""
grade=input("请输入你的分数：")
while grade != "e":
    grade=int(grade)
    if grade < 60:
        print("D")
    elif 60 <= grade < 80:
        print("C")
    elif 80 <= grade < 90:
        print("B")
    elif 90 <= grade < 100:
        print("A")
    else:
        print("S")
    grade = input("请输入你的分数：")

"""改进小游戏下"""
import random
print(random.randint(1,10))

