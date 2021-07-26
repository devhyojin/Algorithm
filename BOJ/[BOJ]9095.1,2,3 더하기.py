from sys import stdin
t=int(stdin.readline())
inputs = [int(stdin.readline()) for _ in range(t)]
max_n=max(inputs)
dp=[0]*(max_n+1)
dp[1],dp[2],dp[3] = 1,2,4
answers=[]
for i in range(4, max_n+1):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
for input in inputs:
    print(dp[input])

    # dp=[0]*(n+1)
    # dp[1], dp[2], dp[3] = 1, 2, 4
    # for i in range(2, n+1):
    #     print(sum([dp[j] for j in range(1,i)]))
    #     dp[i] = (i-1)+sum([dp[j] for j in range(1,i)])
    #     print('ddf', i, dp[i])
    # print('답')
    # print(dp[n])