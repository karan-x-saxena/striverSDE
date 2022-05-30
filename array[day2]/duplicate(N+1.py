def duplicateN_1(arr):
    slow = arr[0]
    fast = arr[0]
    slow = arr[slow]
    fast = arr[arr[fast]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

print(duplicateN_1([2,5,9,6,9,3,8,9,7,1]))
