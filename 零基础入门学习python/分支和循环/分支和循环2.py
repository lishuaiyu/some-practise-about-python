"""
作者：Shuaiyu Li
日期：2022年01月14日
"""
x = 520 if "Love" else 404
print(x)

"角谷猜想"
number = int(input('请输入一个整数'))
while number != 1:
    if number % 2 == 0:
        print(int(number),'/2',' = ',int(number/2),sep='')
        number = number/2
    else:
        print(int(number),'*3+1 = ',int(number * 3 + 1),sep='')
        number = number * 3 + 1

'标准答案'
n = int(input("请输入一个正整数："))

while n > 0:
    if n % 2 == 0:
        print(n, "/2 = ", n // 2, sep='')
        n = n // 2
    else:
        print(n, "*3+1 = ", n * 3 + 1, sep='')
        n = n * 3 + 1
    if n == 1:
        break
