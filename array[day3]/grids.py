def grids_recursion(i,j,m,n):
    if i == n and j == m:
        return 1
    elif i > n or j > m:
        return 0
    a = grids_recursion(i+1,j,m,n)
    b = grids_recursion(i,j+1,m,n)
    return a+b

def grids_memoizations(i,j,m,n,dp):
    if i == n and j == m:
        return 1
    elif i > n or j > m:
        return 0
    if dp[i][j] != -1: return dp[i][j]
    a = grids_memoizations(i + 1, j, m, n,dp)
    b = grids_memoizations(i, j + 1, m, n,dp)
    dp[i][j] = a+b
    return dp[i][j]
m=2
n=2
dp=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
print(grids_memoizations(0,0,m,n,dp))
print(dp)
print(grids_recursion(0,0,m,n))