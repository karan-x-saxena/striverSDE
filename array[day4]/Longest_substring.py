def Longest_Substring(string):
    hashset = set()
    maxi = 0
    l = 0
    for i in range(len(string)):
        if string[i] in hashset:
            while l < i and string[i] in hashset:
                hashset.remove(string[l])
                l = l+1
        hashset.add(string[i])
        maxi = max(maxi,(i-l+1))
    return maxi

print(Longest_Substring("abcabcbb"))