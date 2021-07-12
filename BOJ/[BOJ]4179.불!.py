from sys import stdin
from collections import deque
di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)

def bfs():
    while fire:
        f_ci, f_cj = fire.popleft()
        for dir in range(4):
            f_ni, f_nj = f_ci + di[dir], f_cj + dj[dir]
            if f_ni < 0 or f_ni >= r or f_nj < 0 or f_nj >= c:
                continue
            if fire_dis[f_ni][f_nj] or maze[f_ni][f_nj] == '#':
                continue
            fire.append((f_ni, f_nj))
            fire_dis[f_ni][f_nj] = fire_dis[f_ci][f_cj] + 1
    while jh:
        j_ci, j_cj = jh.popleft()
        for dir in range(4):
            j_ni, j_nj = j_ci + di[dir], j_cj + dj[dir]
            if j_ni < 0 or j_ni >= r or j_nj < 0 or j_nj >= c:
                return jh_dis[j_ci][j_cj] + 1
            if jh_dis[j_ni][j_nj] or maze[j_ni][j_nj] =='#':
                continue
            if fire_dis[j_ni][j_nj] == 0 or jh_dis[j_ci][j_cj]+1 < fire_dis[j_ni][j_nj]:
                jh.append((j_ni, j_nj))
                jh_dis[j_ni][j_nj] = jh_dis[j_ci][j_cj] + 1
    return 'IMPOSSIBLE'

r, c = map(int, stdin.readline().split())
maze = [stdin.readline().rstrip() for _ in range(r)]
fire_dis = [[0]*c for _ in range(r)]
jh_dis = [[0]*c for _ in range(r)]
fire = deque()
jh = deque()
for i in range(r):
    row = stdin.readline().rstrip()
    for j in range(c):
        if maze[i][j] == 'F':
            fire.append((i,j))
        elif maze[i][j] =='J':
            jh.append((i,j))

print(bfs())