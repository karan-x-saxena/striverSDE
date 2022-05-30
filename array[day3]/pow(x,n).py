def Pow(x,n):
    a = 1
    if n < 0:
        n = abs(n)
    while n >= 1:
        if n%2 == 0:
            x = x*x
            n = n/2
        else:
            a = a*x
            n = n-1
    if n < 0:
        return 1/a
    return a
print(pow(2,-2))