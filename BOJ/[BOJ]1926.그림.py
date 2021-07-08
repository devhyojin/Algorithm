from sys import stdin
from collections import deque
def bfs(si, sj):
    queue = deque()
    queue.append((si,sj))
    visited[si][sj] = 1
    area = 0
    while queue:
        ci, cj = queue.popleft()
        area += 1
        for dir in range(4):
            ni, nj = ci+di[dir], cj+dj[dir]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if paper[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni,nj))
    return area

n, m = map(int, stdin.readline().split())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
di = (-1, 0, 1, 0)
dj = (0, -1, 0, 1)
ans_list = []
for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            ans_list.append(bfs(i,j))
print(len(ans_list))
if ans_list:
    print(max(ans_list))
else:
    print(0)
