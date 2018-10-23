# Python code to find number of unique paths in a  matrix with obstacles.


def getPaths(GRID):
    n = len(GRID)
    m = len(GRID[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # initialize start point
    if GRID[0][0] == 1:
        dp[0][0] = 1
    # initialize first row
    for i in range(1,m):
        if GRID[0][i] == 1:
            dp[0][i] = dp[0][i-1]

    # initialize first column
    for i in range(1,n):
        if GRID[i][0] == 1:
            dp[i][0] = dp[i-1][0]
    for i in range(1, n):       # row
        if GRID[i][0] == 1:
            dp[i][0] = dp[i-1][0]
        for j in range(1, m):  # column
            if GRID[i][j] == 1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # print(dp)
    return dp[-1][-1]


A = [[0, 0, 1,1], [0, 1, 1,1], [1, 1, 1,1]]
print(getPaths(A))
