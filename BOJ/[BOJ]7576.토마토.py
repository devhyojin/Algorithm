from sys import stdin
from collections import deque

di = (-1,0,1,0)
dj = (0,1,0,-1)
def bfs():
    done = 0
    ans = 0
    while queue:
        ci, cj, cnt = queue.popleft()
        done += 1
        ans = cnt
        for dir in range(4):
            ni, nj = ci+di[dir], cj+dj[dir]
            if ni < 0 or ni >=n or nj < 0 or nj >= m:
                continue
            if distance[ni][nj] >= 0:
                continue
            distance[ni][nj] = 1
            queue.append((ni, nj, cnt+1))

    if done == tomato_done + tomato_yet:
        return ans
    else:
        return -1

m,n = map(int, stdin.readline().split())
tomatoes = []
distance = [[0]*m for _ in range(n)]
queue = deque()
tomato_done = 0
tomato_yet = 0
for i in range(n):
    tomatoes.append(list(map(int, stdin.readline().split())))
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i,j,0))
            tomato_done += 1
        elif tomatoes[i][j] == 0:
            distance[i][j] = -1
            tomato_yet += 1
if tomato_done == tomato_done + tomato_yet:
    print(0)
else:
    print(bfs())
