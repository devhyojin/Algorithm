def solution(money):
    n = len(money)
    #1집 털음, 1집 패스
    dp1, dp2 = [money[0]]+[0 for _ in range(n-1)], [0 for _ in range(n)]
    for i in range(1, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    dp2[n-1] = max(dp2[n-2], dp2[n-3]+money[n-1])
    return max(dp1[n-2], dp2[n-1])