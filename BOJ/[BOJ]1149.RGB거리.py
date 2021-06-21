from sys import stdin
n = int(stdin.readline())
costs = list(list(map(int, stdin.readline().split())) for _ in range(n))
for i in range (1, n):
    # 빨간집 처음 고를 경우
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    # 초록집 처음 고를 경우
    costs[i][1] = min(costs[i - 1][0], costs[i - 1][2]) + costs[i][1]
    # 파란집 처음 고를 경우
    costs[i][2] = min(costs[i - 1][0], costs[i - 1][1]) + costs[i][2]
print(min(costs[n-1]))