def kadane_algo(arr,subarr):
    mep = 0
    msp = arr[0]
    start = 0
    for end in range(len(arr)):
        mep = mep+arr[end]
        if mep > msp:
            subarr.clear()
            msp = mep
            subarr.append(start)
            subarr.append(end)
        if mep < 0:
            mep = 0
            start = end + 1
    return msp

def launch_kadane(arr):
    sub = []
    ans = kadane_algo(arr,sub)
    temp = []
    for i in range(sub[0],sub[1]+1):
        temp.append(arr[i])
    return [ans,temp]
print(launch_kadane([-2,1,-3,4,-1,2,1,-5,4]))