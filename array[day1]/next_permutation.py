def laxo_permu(arr):
    i = len(arr)-2
    j = 0
    while i >=0:
        if arr[i] < arr[i+1]:
            j = i
            i = 1
            break
        i = i-1
    if i < 0:
        arr.reverse()
        return
    i = j
    l = len(arr)-1
    while l > i:
        if arr[l] > arr[i]:
            break
        l = l-1
    temp = arr[i]
    arr[i] = arr[l]
    arr[l] = temp
    new_arr = arr[0:i+1]
    for_sort = arr[i+1:len(arr)]
    for_sort.sort()
    arr[:] = new_arr + for_sort

arr1 = [2,3,1]
arr = [1,3,2,6,5,4]
laxo_permu(arr1)
print(arr1)