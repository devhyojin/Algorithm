from sys import stdin
from collections import deque

di = (-1, 1, 2, 2, -1, 1, -2, -2 )
dj = (2, 2, -1, 1, -2, -2, -1, 1)

def bfs(si, sj, ei, ej):
    queue = deque()
    queue.append((si,sj))
    while queue:
        ci, cj = queue.popleft()
        if ci == ei and cj == ej:
            return board[ci][cj]
        for d in range(8):
            ni, nj = ci+di[d], cj+dj[d]
            if 0<= ni < l and 0 <= nj < l and not board[ni][nj]:
                queue.append((ni,nj))
                board[ni][nj] = board[ci][cj] + 1

n = int(stdin.readline())
for _ in range(n):
    l = int(stdin.readline())
    cur_i, cur_j = map(int, stdin.readline().split())
    next_i, next_j = map(int, stdin.readline().split())
    board = [[0 for _ in range(l)] for _ in range(l)]
    ans = 0
    if cur_i != next_i or cur_j != next_j:
        ans = bfs(cur_i, cur_j, next_i, next_j)
    print(ans)




