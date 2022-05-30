def merge_overlap(arr):
    j = 0
    i = 1
    arr.sort()
    while i < len(arr):
        if arr[j][1] >= arr[i][0] and arr[j][1] <= arr[i][1]:
            arr[j][1] = arr[i][1]
            arr.pop(i)
        elif arr[j][1] >= arr[i][0] and arr[j][1] >= arr[i][1]:
            arr.pop(i)
        else:
            j = j+1
            i = i+1
arr = [[1,3],[2,6],[8,10],[15,18]]
merge_overlap(arr)
print(arr)
