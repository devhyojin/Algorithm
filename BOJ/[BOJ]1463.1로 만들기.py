from sys import stdin
n=int(stdin.readline())
dp=[0]*(n+1)
dp[1] = 0
for i in range(2,n+1):
    dp[i] = dp[i-1]+1 #이전 수에서 1을 더한 것(연산3)과 같다.
    if not i%3: #연산1
        dp[i] = min(dp[i], dp[i//3]+1)
        continue
    if not i%2: #연산2
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])

