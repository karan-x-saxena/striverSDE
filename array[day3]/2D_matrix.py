def D2_matrix(mat,target):
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = (n*m)-1
    while high >= low:
        mid = (low+high)//2
        if mat[mid//m][mid%m] > target:
            high = mid-1
        elif mat[mid//m][mid%2] < target:
            low = mid+1
        else:
            return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(D2_matrix(matrix,15))