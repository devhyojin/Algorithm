from sys import stdin
from collections import deque

dr = (-1,0,1,0)
dc = (0,1,0,-1)

def bfs(sr,sc):
    queue = deque()
    queue.append((sr,sc))
    visited[sr][sc] = True
    while queue:
        cr, cc = queue.popleft()
        for dir in range(4):
            nr, nc = cr+dr[dir], cc+dc[dir]
            if nr<0 or nr>=n or nc<0 or nc>=m:
                continue
            if farm[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr,nc))

t = int(stdin.readline())
for _ in range(t):
    m,n,k = map(int, stdin.readline().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    cabbages = []
    larva = 0
    for _ in range(k):
        b, a = map(int, stdin.readline().split())
        farm[a][b] = 1
        cabbages.append((a,b))
    for cabbage in cabbages:
        r, c = cabbage
        if not visited[r][c]:
            bfs(r,c)
            larva += 1
    print(larva)

