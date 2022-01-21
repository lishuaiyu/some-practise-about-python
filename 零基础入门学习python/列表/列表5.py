###通过for循环创建并初始化二维列表
from itertools import count
from os import major
from pyparsing import nums
from sympy import count_ops


A =[0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A)

for i in range(3):
    for j in range(3):
        A[i][j]=[0] * 3
print(A)


###改进的摩尔投票法###
nums = [1, 1, 2, 1, 3, 2, 3, 2]

##对抗阶段##
major1 = nums[0]
major2 = nums[0]
count1 = 0
count2 = 0

for i in nums:
    if major1 == i:
        count1 += 1
        continue
    if count1 == 0:
        major1 = i
        count1 = 1
        continue
    count1 -= 1
    
    if major2== i:
        count2 += 1
        continue
    if count2 == 0:
        major2 = i
        count2 = 1
        continue
    count1 -= 1
    count2 -= 1
    
# 统计阶段
if nums.count(major1) > len(nums) / 3:
    print(major1)
if nums.count(major2) > len(nums) / 3:
    print(major2)
    
    
nums = [1, 1, 2, 1, 3, 2, 3, 2]
   
major1 = major2 = nums[0]
count1 = count2 = 0
   
# 对抗阶段
for each in nums:
    if major1 == each:
        count1 += 1
        continue
   
    if major2 == each:
        count2 += 1
        continue
   
    if count1 == 0:
        major1 = each
        count1 = 1
        continue
   
    if count2 == 0:
        major2 = each
        count2 = 1
        continue
   
    count1 -= 1
    count2 -= 1
   
# 统计阶段
if nums.count(major1) > len(nums) / 3:
    print(major1)
if nums.count(major2) > len(nums) / 3:
    print(major2)