
arr=[4,1,5,2,3]

for i in range (len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)