from sys import stdin

dr=(-1,0,1,0)
dc=(0,1,0,-1)

def friend_cond():
    position, max_cnt=[], 0
    for r in range(n):
        for c in range(n):
            if board[r][c] ==0:
                cnt=0
                for dir in range(4):
                    nr, nc = r+dr[dir], c+dc[dir]
                    if nr<0 or nr>=n or nc<0 or nc>=n:
                        continue
                    if board[nr][nc] in friends:
                        cnt+=1
                if max_cnt < cnt:
                    max_cnt = cnt
                    position = [(r,c)]
                elif max_cnt == cnt:
                    position.append((r,c))
    if len(position) == 1:
        return position.pop()
    else:
        return blank_cond(position)
def blank_cond(p_list):
    position, max_cnt = [], 0
    if len(p_list):
        for cr, cc in p_list:
            cnt = 0
            for dir in range(4):
                nr, nc = cr+dr[dir], cc+dc[dir]
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                if board[nr][nc] == 0:
                    cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
                position = [(cr, cc)]
            elif max_cnt == cnt:
                position.append((cr, cc))
    else:
        for r in range(n):
            for c in range(n):
                cnt = 0
                for dir in range(4):
                    nr, nc = r + dr[dir], c + dc[dir]
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue
                    if board[nr][nc] == 0:
                        cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
                    position = [(r, c)]
                elif max_cnt == cnt:
                    position.append((r, c))

    if len(position) == 1:
        return position.pop()
    elif len(position) > 1:
        return min_cond(position)

def min_cond(p_list):
    p_list.sort(key=lambda x: (x[0],x[1]))
    return p_list[0]

def satisfied():
    satisfaction = 0
    for r in range(n):
        for c in range(n):
            cur = board[r][c]
            cnt = -1
            for dir in range(4):
                nr, nc = r + dr[dir], c + dc[dir]
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                if board[nr][nc] in favorites[cur]:
                    cnt+=1
            if cnt != -1:
                satisfaction += 10**cnt
    return satisfaction

n=int(stdin.readline())
nn = n**2
board = [[0 for _ in range(n)] for _ in range(n)]
favorites = [[] for _ in range(nn + 1)]
for i in range(nn):
    temp = list(map(int, stdin.readline().split()))
    me,friends = temp[0], temp[1:]
    favorites[me] = friends
    if i == 0:
        a, b = blank_cond([])
    else:
        a, b = friend_cond()
    board[a][b] = me

print(satisfied())
