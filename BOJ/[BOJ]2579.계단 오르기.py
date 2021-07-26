#백트래킹
from sys import stdin

def dynamic():
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1][1], dp[1][2] = stairs[1], 0
    dp[2][1], dp[2][2] = stairs[2], dp[1][1] + stairs[2]
    if n == 1:
        return stairs[1]
    for i in range(3, n + 1):
        dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + stairs[i]
        dp[i][2] = dp[i - 1][1] + stairs[i]
    return max(dp[n][1],dp[n][2])

n=int(stdin.readline())
stairs=[0]+ list(int(stdin.readline()) for _ in range(n))
print(dynamic())
#백트래킹(n이 300이어서 백트래킹 사용 시 시간초과가 일어난다.)
# from sys import stdin
#
# def sol(idx, score, cnt):
#     global max_score
#     if idx > -1:
#         score += stairs[idx]
#     if idx <= 0:
#         max_score = max(max_score, score)
#         return
#     if cnt < 1:
#         sol(idx-1,score, cnt+1)
#     sol(idx-2,score, 0)
#
# n=int(stdin.readline())
# stairs=list(int(stdin.readline()) for _ in range(n))
# max_score = 0
# sol(n-1,0, 0)
# print(max_score)