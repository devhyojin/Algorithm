from sys import stdin
n,m=map(int, stdin.readline().split())
nums=[0]+list(map(int, stdin.readline().split()))
cur_sum = 0
dp=[0]*(n+1)
for a in range(1, n+1):
    cur_sum += nums[a]
    dp[a] = cur_sum

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(dp[j]-dp[i-1])
