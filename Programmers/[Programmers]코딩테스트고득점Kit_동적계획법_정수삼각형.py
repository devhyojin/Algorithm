def solution(triangle):
    n = len(triangle)
    dp=[[0 for _ in range(i+1)] for i in range(n)]
    dp[0]=triangle[0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0]+triangle[i][0]
        dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
        for j in range(1,len(triangle[i])-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
    return max(dp[n-1])