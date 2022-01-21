"""
作者：Shuaiyu Li
日期：2022年01月14日
"""
"""浮点数"""
print(0.1+0.2)
print(0.1+0.2==0.3)

import decimal
a=decimal.Decimal('0.1')
b=decimal.Decimal('0.2')
c=decimal.Decimal('0.3')
print(a+b==c)

x=1+2j
print(x)
print(x.imag)
print(x.real)
