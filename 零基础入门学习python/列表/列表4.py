from itertools import count
from os import major
from numpy import ma

from pyparsing import nums


print([[1, 2, 3], [4, 5, 6]] + [7, 8, 9])

a = 1000
b = 1000
print(a is b)

list = [2, 2, 4, 2, 3, 6, 2]
list.sort()
length = len(list)
half = list[length // 2]
count = 0

for i in list:
    if i == half:
        count = count + 1 
if count >= length / 2:
    print("存在主要元素，是：",half)
else:
    print("不存在主要元素")


###摩尔投票法###
  
nums = [2, 2, 4, 2, 3, 6, 2]

##对抗阶段##
major = nums[0]
count = 0
for i in nums: 
    if count == 0:
        major = i
    if i == major:
        count += 1
    if i != major:
        count -= 1
    

##生成阶段##
if nums.count(major) > len(nums) / 2:
    print("主要元素是：", major)
else:
    print("不存在主要元素。")