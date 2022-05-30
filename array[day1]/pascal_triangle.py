def pascal_triangle(n):
    arr = [[1]]
    for i in range(n):
        temp = []
        for j in range(len(arr)+1):
            if j == 0:
                temp.append(1)
            elif j == len(arr):
                temp.append(1)
            else:
                a = arr[i][j-1] + arr[i][j]
                temp.append(a)
        arr.append(temp)
    return arr

def pascal_triangle_element(n,m):
    if m == 0: return 1.0
    a = n
    b = 1
    i = 1
    j = n
    while i <m:
        a = a*(j-1)
        b = b*(i+1)
        i = i+1
        j = j-1
    return a/b

def pascal_trianglr_row(n):
    temp = [1.0]
    a = n
    b = 1
    i = 1
    j = n
    while i<4:
        a = a * (j - 1)
        b = b * (i + 1)
        i = i + 1
        j = j - 1
        temp.append(a/b)
    return temp

print(pascal_triangle(5))
print(pascal_trianglr_row(5))
print(pascal_triangle_element(4,2))