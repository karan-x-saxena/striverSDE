def Majority_n2(arr):
    count = 0
    ans = 0
    for i in range(len(arr)):
        if count == 0:
            ans = arr[i]
            count = count+1
        elif arr[i] != ans:
            count = count-1
        else:
            count = count+1
    return ans
print(Majority_n2([]))