def Two_sum(arr,target):
    unorder = {}
    for i in range(len(arr)):
        check = target - arr[i]
        if check in unorder:
            return [unorder[check],i]
        unorder.update({arr[i]:i})
    return -1

print(Two_sum([3,2,4,6],6))