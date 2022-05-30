def sort_0_1_2(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while mid < high:
        if arr[mid] == 0:
            temp = arr[mid]
            mid = arr[low]
            arr[low] = temp
            mid = mid+1
            low = low+1
        elif arr[mid] == 2:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high = high-1
        else:
            mid = mid+1
kar = [2,0,2,1,1,0]
sort_0_1_2(kar)
print(kar)