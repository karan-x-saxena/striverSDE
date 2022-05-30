def subarray_XOR(arr,target):
    unorder = {}
    count = 0
    xor = 0
    for i in range(len(arr)):
        xor = xor^arr[i]
        if xor == target:
            count = count+1
        temp = xor^target
        if temp in unorder:
            count = count + unorder[temp]
            unorder[temp] = unorder[temp]+1
        if xor in unorder:
            unorder[xor] = unorder[xor]+1
        else:
            unorder.update({xor:1})
    return count

print(subarray_XOR([4, 2, 2, 6, 4],6))