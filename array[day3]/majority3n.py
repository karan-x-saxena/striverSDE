def Majority_3n(arr):
    unorder = {}
    ans = []
    for i in range(len(arr)):
        if arr[i] in unorder:
            increase = unorder[arr[i]] + 1
            unorder.update({arr[i]:increase})
        else:
            unorder.update({arr[i]:1})
    for i in unorder:
        if unorder[i] > len(arr)//3:
            ans.append(i)
    return ans
print(Majority_3n([11,33,33,11,33,11]))