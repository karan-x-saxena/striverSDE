# 100, 200, 1,2,3,4
def Longest_consecutive(arr):
    hashset = set()
    for i in range(len(arr)):
        hashset.add(arr[i])
    maxi = 0
    for i in arr:
        if i-1 in hashset:
            continue
        else:
            current = i
            count = 0
            while current in hashset:
                count = count+1
                current = current+1
            maxi = max(maxi,count)
    return maxi

print(Longest_consecutive([100,200,1,2,3,4]))