def repeating(arr):
    n = len(arr)
    x = (n*(n+1))/2
    p1 = (n*(n+1)*((2*n)+1))/6
    y = 0
    p2 = 0
    for i in range(len(arr)):
        y = y+arr[i]
        p2 = p2+(arr[i]*arr[i])
    p = p1-p2
    s = x-y
    miss = ((p/s)+s)/2
    repeat = miss-s
    return [miss,repeat]

print(repeating([3,1,2,5,3]))