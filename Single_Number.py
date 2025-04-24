# nums = [2, 2, 1]
#
#
# for i in nums:
#     if nums.count(i)==1:
#         print(i)
#         break

nums = [1,2,1,3,2,5]
a=[]
for i in nums:
    if nums.count(i)==1:
        a.append(i)
print(a)
