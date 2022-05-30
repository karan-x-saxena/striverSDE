def merge_sortedArray(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    diff = (n+m)//2
    while diff > 0:
        i = 0
        j = diff
        while j < (n+m):
            if j < n and arr1[i] > arr1[j]:
                temp = arr1[i]
                arr1[i] = arr1[j]
                arr1[j] = temp
            elif j >= n and i<n and arr1[i] > arr2[j-n]:
                temp1 = arr1[i]
                arr1[i] = arr2[j-n]
                arr2[j-n] = temp1
            elif j >=n and i>=n and arr2[i-n] > arr2[j-n]:
                temp2 = arr2[i-n]
                arr2[i-n] = arr2[j-n]
                arr2[j-n] = temp2
            i = i+1
            j = j+1
        diff = diff//2

arr1 = [1,4 ,8 ,10]
arr2 = [2 ,3 ,9]
merge_sortedArray(arr1,arr2)
print(arr1,arr2)