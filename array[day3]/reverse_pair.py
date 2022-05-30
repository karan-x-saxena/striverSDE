def Merge(arr,low,mid,high):
    count = 0
    j = mid
    i = low

    while j <= high:
        while i <= mid-1 and arr[i] <= 2*arr[j]:
            i = i+1
        count = count+(mid-i)
        j = j+1
    temp = []
    left = low
    right = mid

    while left <= mid-1 and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left = left+1
        else:
            temp.append(arr[right])
            right = right+1

    while left <=mid-1:
        temp.append(arr[left])
        left = left+1

    while right <= high:
        temp.append(arr[right])
        right = right+1
    k = low
    while k <= high:
        arr[k] = temp[k-low]
        k = k+1
    return count

def Merge_sort(arr,low,high):
    count = 0
    if high > low:
        mid = (high+low)//2
        count = count + Merge_sort(arr,low,mid)
        count = count + Merge_sort(arr,mid+1,high)
        count = count + Merge(arr,low,mid+1,high)
    return count

arr = [40,25,19,12,9,6,2]
print(Merge_sort(arr,0,len(arr)-1))