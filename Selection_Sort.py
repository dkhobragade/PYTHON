
arr=[4,1,5,2,3]

for i in range(len(arr)):
    small = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[small]:
              small = j

    arr[i],arr[small] = arr[small],arr[i]
print(arr)
