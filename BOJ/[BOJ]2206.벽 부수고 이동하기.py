#벽 부수는 방식 수정 필요
from sys import stdin
from collections import deque

dr=(-1,0,1,0)
dc=(0,1,0,-1)

def bfs(r, c):
    change = 1
    queue = deque()
    queue.append((r,c))
    visited[r][c] = 1
    while queue:
        cr, cc = queue.popleft()
        for dir in range(4):
            nr, nc = cr+dr[dir], cc+dc[dir]
            if nr<0 or nr>=n or nc<0 or nc>=m:
                continue
            if board[nr][nc]=='0' and not visited[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + 1
                queue.append((nr, nc))
        if not queue:
            for dir in range(4):
                nr, nc = cr + dr[dir], cc + dc[dir]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if not visited[nr][nc] and change:
                    change -= 1
                    visited[nr][nc] = visited[cr][cc] + 1
                    queue.append((nr, nc))


n,m = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
bfs(n-1,m-1)
if visited[0][0]:
    print(visited[0][0])
else:
    print(-1)