def four_sum(arr,target):
    arr.sort()
    ans = []
    for i in range(len(arr)):
        pointer1 = arr[i]
        target1 = target - pointer1
        j = i+1
        while j in range(len(arr)):
            pointer2 = arr[j]
            target2 = target1 - pointer2
            front = j+1
            back = len(arr)-1
            while back > front:
                twosum = arr[front]+arr[back]
                if twosum < target2:
                    front = front+1
                elif twosum > target2:
                    back = back-1
                else:
                    ans.append([arr[i],arr[j],arr[front],arr[back]])
                    f = arr[front]
                    b = arr[back]

                    while front < back and arr[front] == f:
                        front = front+1
                    while back > front and arr[back] == b:
                        back = back-1
            while j+1<len(arr) and arr[j] == arr[j+1]:
                j = j+1
            j = j+1
        while i+1 < len(arr) and arr[i] == arr[i+1]:
            i = i+1
    return ans

print(four_sum([1,0,-1,0,-2,2],0))