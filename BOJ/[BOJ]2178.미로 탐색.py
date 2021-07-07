from sys import stdin
from collections import deque

def bfs(si,sj,ei,ej):
    di = (-1,0,1,0)
    dj = (0,1,0,-1)
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append((si,sj))
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        if ci == ei and cj == ej:
            return visited[ci][cj]
        for d in range(4):
            ni, nj = ci+di[d], cj+dj[d]
            if 0<=ni<n and 0<=nj<m and maze[ni][nj] == '1' and not visited[ni][nj]:
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni,nj))


n, m = map(int, stdin.readline().split())
maze = [stdin.readline().rstrip() for _ in range(n)]
print(bfs(0,0,n-1,m-1))