def merge(arr,temp,left,mid,right):
    count = 0
    i = left
    j = mid
    while i<=mid-1 and j<=right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i = i+1
        else:
            temp.append(arr[j])
            count = count+1
            j = j+1
    while i<=(mid-1):
        temp.append(arr[i])
        i = i+1
    while j<=right:
        temp.append(arr[j])
        j = j+1
    i = left
    while i <= right:
        arr[i] = temp[i]
        i = i+1
    return count

def merge_sort(arr,temp,left,right):
    mid = 0
    count = 0
    if right>left:
        mid = (left+right)//2
        count = count + merge_sort(arr,temp,left,mid)
        count = count+ merge_sort(arr,temp,mid+1,right)
        count = count+ merge(arr,temp,left,mid+1,right)
    return count

arr = [5,3,2,1,4]
print(merge_sort(arr,[],0,len(arr)-1))