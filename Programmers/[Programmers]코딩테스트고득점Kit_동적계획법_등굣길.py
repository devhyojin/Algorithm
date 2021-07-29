def solution(m, n, puddles):
    dp=[[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for a in range(n):
        for b in range(m):
            if ([b+1,a+1] in puddles) or ((a,b)==(0,0)):
                continue
            dp[a][b]=(dp[a-1][b]+dp[a][b-1]) % 1000000007
    return dp[n-1][m-1]