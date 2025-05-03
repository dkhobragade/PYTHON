arr = [1, 2, 3, 4, 5]
k = 4

low = 0
high = len(arr)-1

while low<=high:
    mid = (low+high)//2

    if arr[mid]==k:
        print(mid)
        break
    elif arr[mid]<k:
        low=mid+1
    else:
        high=mid-1

