#백트래킹
from sys import stdin

def backtracking(day, profit):
    global max_profit, check
    if day > n-1:
        max_profit = max(max_profit, profit)
        return
    next = day + info[day][0]
    if next < n+1:
        sol(next, profit+info[day][1])
    sol(day+1, profit)


n=int(stdin.readline())
info = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
max_profit = 0
backtracking(0,0)
print(max_profit)

#dp
from sys import stdin

def dp():
    memo = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        temp = i + info[i][0]
        if temp > n:
            memo[i] = memo[i+1]
        else:
            memo[i] = max(info[i][1] + memo[temp], memo[i+1])
    return memo[0]

n=int(stdin.readline())
info = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
print(dp())