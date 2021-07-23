from sys import stdin
from collections import deque

dr=(-1,0,1,0)
dc=(0,1,0,-1)

def bfs():
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0,0,1))
    visited[0][0][1] = 1
    while queue:
        cr, cc, flag = queue.popleft()
        if cr == n-1 and cc == m-1:
            return visited[cr][cc][flag]
        for dir in range(4):
            nr, nc = cr+dr[dir], cc+dc[dir]
            if nr<0 or nr>=n or nc<0 or nc>=m:
                continue
            if board[nr][nc]==1 and flag==1:
                queue.append((nr, nc, 0))
                visited[nr][nc][0] = visited[cr][cc][1] + 1
            elif board[nr][nc]==0 and visited[nr][nc][flag]==0:
                queue.append((nr, nc, flag))
                visited[nr][nc][flag] = visited[cr][cc][flag] + 1
    return -1

n,m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
print(bfs())