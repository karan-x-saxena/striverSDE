def rotate_90(arr):
    for i in range(len(arr)):
        for j in range(i):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
    for i in arr:
        i.reverse()
    return
kar = [[1,2,3],[4,5,6],[7,8,9]]
rotate_90(kar)
print(kar)