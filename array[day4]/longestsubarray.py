def Longest_subarray(arr):
    unorder = {}
    maxi = 0
    sume = 0
    for i in range(len(arr)):
        sume = sume + arr[i]
        if sume == 0:
            maxi = i+1
        if sume in unorder:
            count = i-unorder[sume]
            maxi = max(maxi,count)
        else:
            unorder.update({sume:i})
    return maxi

print(Longest_subarray([9, -3, 3, -1, 6, -5]))