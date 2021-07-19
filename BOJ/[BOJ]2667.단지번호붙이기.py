from sys import stdin
from collections import deque

dr = (-1,0,1,0)
dc = (0,1,0,-1)

def dfs():
    cnt = 1
    while queue:
        cr, cc = queue.popleft()
        for dir in range(4):
            nr, nc = cr+dr[dir], cc+dc[dir]
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            if area[nr][nc] == '1' and not visited[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = True
                cnt += 1
    return cnt


n = int(stdin.readline())
area = [stdin.readline().rstrip() for _ in range(n)]
queue = deque()
visited = [[False]*n for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if area[i][j] == '1' and not visited[i][j]:
            queue.append((i,j))
            visited[i][j] = True
            ans.append(dfs())

print(len(ans))
for a in sorted(ans):
    print(a)