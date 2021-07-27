#dp1 (밟을 계단 선택하기)
# from sys import stdin
#
# def dynamic():
#     dp = [[0, 0] for _ in range(n + 1)]
#     dp[1][0], dp[1][1] = stairs[1], 0
#     dp[2][0], dp[2][1] = stairs[2], stairs[1] + stairs[2]
#     dp[3][0], dp[3][1] = stairs[1]+stairs[3], stairs[2]+stairs[3]
#     for i in range(4, n + 1):
#         dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + stairs[i]
#         dp[i][1] = dp[i - 1][0] + stairs[i]
#     return max(dp[n][0],dp[n][1])
#
# n=int(stdin.readline())
# stairs= [0] + list(int(stdin.readline()) for _ in range(n))
# if n == 1:
#     print(stairs[1])
# elif n == 2:
#     print(stairs[1]+stairs[2])
# elif n == 3:
#     print(max(stairs[1], stairs[2])+stairs[3])
# else:
#     print(dynamic())

#dp2 (밟지 않을 계단 최소값으로 선택하기)
from sys import stdin
n=int(stdin.readline())
stairs= [0] + list(int(stdin.readline()) for _ in range(n))

def dp():
    dp= [0 for _ in range(n+1)]
    dp[1]=stairs[1]
    dp[2]=stairs[2]
    dp[3]=stairs[3]
    for i in range(4, n+1):
        dp[i]=min(dp[i-3], dp[i-2])+stairs[i]
    return sum(stairs)-min(dp[n-1], dp[n-2])

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1]+stairs[2])
elif n == 3:
    print(max(stairs[1], stairs[2])+stairs[3])
else:
    print(dp())
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