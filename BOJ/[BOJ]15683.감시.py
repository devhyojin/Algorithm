from sys import stdin

dr=(1,0,-1,0)
dc=(0,1,0,-1)

def detect(r,c, direction):
    global board
    cnt = 0
    while True:
        nr, nc = r + dr[direction], c + dc[direction]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or temp[nr][nc]==6:
            return cnt
        # cctv가 있거나, 이미 감지한 공간이면 지나치자
        if 0 < temp[nr][nc] < 6 or temp[nr][nc] == -1:
            r,c=nr,nc
            continue
        # 감지했으면 표시하자
        temp[nr][nc] = -1
        cnt+=1
        r,c=nr,nc
    return cnt

def dfs(num):
    global blind
    if num == len(cctv):
        cnt = 0
        for i in range(len(cctv)):
            r, c, case = cctv[i]
            if case == 1:
                cnt += detect(r,c,dir[i])
            elif case == 2:
                cnt += detect(r,c,dir[i])
                cnt += detect(r,c,(dir[i]+2)%4)
            elif case == 3:
                cnt += detect(r,c,dir[i])
                cnt += detect(r,c,(dir[i]+1)%4)
            else:
                cnt += detect(r,c,dir[i])
                cnt += detect(r,c,(dir[i]+1)%4)
                cnt += detect(r,c,(dir[i]+2)%4)
        blind = min(blind, blind-cnt)
        return
    for i in range(4):
        dfs(num+1)
    return blind


n, m = map(int, stdin.readline().split())
board, cctv, cctv5 = [], [], []
detected=[[0 for _ in range(m)] for _ in range(n)]
blind = n*m
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    board.append(temp)
    for j in range(m):
        if 0 < temp[j] < 5:
            cctv.append((i,j,temp[j]))
            blind -= 1
        elif temp[j] == 5:
            cctv.append((i,j))
            blind -= 1
        elif temp[j] == 6:
            blind -= 1

# cctv5가 감시하는 지역 모두 detect
for i in range(len(cctv5)):
    r, c = cctv5[i]
    for dir in range(4):
        while True:
            nr, nc = r+dr[dir], c+dc[dir]
            if nr<0 or nr>=n or nc<0 or nc>=m:
                break
            # cctv가 있거나, 이미 감지한 공간이면 지나치자
            if 0<board[nr][nc]<6 or board[nr][nc] == -1:
                continue
            # 감지했으면 표시하자
            board[nr][nc] = -1
            blind -= 1

print(dfs(0))


