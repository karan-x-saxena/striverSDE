def set_matrix(mat):
    curr = 1
    for i in range(len(mat)):
        if mat[i][0] == 0:
            curr = 0
        j = 1
        while j in range(len(mat[0])):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
            j = j+1
    i = len(mat)-1
    while i >= 0:
        j = len(mat[0]) - 1
        while j >= 1:
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
            j = j-1
        if curr == 0:
            mat[i][0] = 0
        i = i-1
    return mat
mat=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix(mat)
print(mat)