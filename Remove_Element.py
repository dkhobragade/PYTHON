nums = [3,2,2,3]
val = 3

count =0

for i in nums:
    if i != val :
        nums[count] = val
        count += 1

print(count)