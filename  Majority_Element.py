import math
from math import floor

nums = [3,2,3]

# print(math.ceil(len(nums)/2))
# for i in nums:
#     if nums.count(i)==math.ceil(len(nums)/2):
#         print(i)


nums.sort()
print(nums[len(nums)//2])