nums = [1,3,5,6]
target = 2

count = 0
if target in nums:
    print(nums.index(target))
else:
    for i in range(len(nums)):
        if target < nums[i]:
            count = i
            break
    print(count+1)
    print(len(nums)-1)


