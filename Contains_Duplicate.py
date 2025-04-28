nums = [1,2,3,1]

for i in nums:
    if nums.count(i)>1:
        print("DUPLICATE")
        break
print("NO DUPLICATE")