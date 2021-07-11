from sys import stdin
from collections import deque
di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)

def bfs():
    while fire:
        f_ci, f_cj = fire.popleft()
        for dir in range(4):
            f_ni, f_nj = f_ci + di[dir], f_cj + dj[dir]
            if f_ni < 0 or f_ni >= c or f_nj < 0 or f_nj >= r:
                continue
            if fire_dis[f_ni][f_nj] == 0:
                fire.append((f_ni, f_nj))
                fire_dis[f_ni][f_nj] = fire_dis[f_ci][f_cj] + 1
    return

def bfs1(fire_dis):
    ans = 0
    while jh:
        j_ci, j_cj = jh.popleft()
        for dir in range(4):
            j_ni, j_nj = j_ci + di[dir], j_cj + dj[dir]
            if j_ni < 0 or j_ni >= c or j_nj < 0 or j_nj >= r and jh_dis[j_ni][j_nj] != -1:
                return fire_dis[j_ci][j_cj]
            if jh_dis[j_ni][j_nj] == 0 and jh_dis[j_ci][j_cj] >= fire_dis[j_ni][j_nj]:
                jh.append((j_ni, j_nj))
                jh_dis[j_ni][j_nj] = jh_dis[j_ci][j_cj] + 1

r, c = map(int, stdin.readline().split())
maze = [stdin.readline().rstrip() for _ in range(c)]
fire_dis = [[0]*r for _ in range(c)]
jh_dis = [[0]*r for _ in range(c)]
fire = deque()
jh = deque()
for i in range(c):
    for j in range(r):
        if maze[i][j] == 'F':
            fire.append((i,j))
            fire_dis[i][j] = 1
        elif maze[i][j] =='J':
            jh.append((i,j))
            jh_dis[i][j] = 1
        elif maze[i][j] == '#':
            fire_dis[i][j] = -1
            jh_dis[i][j] = -1
bfs()
print(bfs1(fire_dis))
