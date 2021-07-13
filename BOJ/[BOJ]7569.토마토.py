from sys import stdin
from collections import deque
di = (-1,0,0,0,0,1)
dj = (0,-1,0,0,1,0)
dk = (0,0,-1,1,0,0)
def bfs():
    while queue:
        ci, cj, ck = queue.popleft()
        for dir in range(6):
            ni, nj, nk = ci+di[dir], cj+dj[dir], ck+dk[dir]
            if ni<0 or ni>=h or nj<0 or nj>=n or nk<0 or nk>=m:
                continue
            if result[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
                queue.append((ni, nj, nk))
                visited[ni][nj][nk] = visited[ci][cj][ck] + 1
                result[ni][nj][nk] = 1

def checker():
    max_day = 0
    for z in range(h):
        for y in range(n):
            if 0 in result[z][y]:
                return -1
            line_max = max(visited[z][y])
            max_day = max(max_day, line_max)
    return max_day - 1

m,n,h = map(int, stdin.readline().split())
result = [[] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = deque()
cannot_done, st = False, False
for i in range(h):
    for j in range(n):
        line = list(map(int, stdin.readline().split()))
        result[i].append(line)
        for k in range(m):
            if line[k] == 1:
                queue.append((i,j,k))
                visited[i][j][k] = 1
bfs()
print(checker())

