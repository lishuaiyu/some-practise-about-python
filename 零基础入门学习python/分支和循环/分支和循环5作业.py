"""
作者：Shuaiyu Li
日期：2022年01月16日
"""
for i in range(10):
    print(i, end=' ')
    i = 5

a, b, c = range(3, 10, 3)
print(a+b+c)

print(len(range(0,10,2)))

result = 0
for each in range(-10,-100,-20):
    result += each
print(result)

for num in range(2,10):
    if num % 2 == 0:
        print(num, "是偶数")
        continue
    print(num, '是奇数')

for num in range(2,10):
    if num % 2 == 0:
        print(num, "是偶数")
        break
    print(num, '是奇数')

for num in range(2,10):
    if num % 2 == 0:
        print(num, "是偶数")
    print(num, '是奇数')
    