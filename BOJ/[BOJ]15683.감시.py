# 수정 필요
from sys import stdin

def up(a, b):
    temp = []
    while a>=0 and office[a][b] != 6:
        a-=1
        temp.append((a,b))
    return temp

def down(a, b):
    temp = []
    while a<n and office[a][b] != 6:
        a+=1
        temp.append((a,b))
    return temp

def left(a, b):
    temp = []
    while b>=0 and office[a][b] != 6:
        b-=1
        temp.append((a,b))
    return temp

def right(a, b):
    temp = []
    while b<m and office[a][b] != 6:
        b+=1
        temp.append((a,b))
    return temp

n,m = map(int, stdin.readline().split())
detected=[[False for _ in range(m)] for _ in range(n)]
office = []
cctv_list = []
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    office.append(temp)
    for j in range(m):
        if temp[j] in (1,2,3,4,5):
            cctv_list.append((temp[j],i,j))

cases=[]
for cctv in cctv_list:
    kind, r, c = cctv
    if kind == 1:
        temp = [up(r,c), down(r,c), left(r,c), right(r,c)]
        cases.append(temp)
    elif kind == 2:
        row = up(r,c)+down(r,c)
        col = left(r,c)+right(r,c)
        temp = [row, col]
        cases.append(temp)
    elif kind == 3:
        up_left = up(r,c)+left(r,c)
        up_right = up(r,c)+right(r,c)
        down_right = right(r,c)+down(r,c)
        down_left = left(r,c)+down(r,c)
        temp = [up_left, up_right, down_right, down_left]
        cases.append(temp)
    elif kind == 4:
        no_up = left(r,c)+right(r,c)+down(r,c)
        no_down = up(r,c)+left(r,c)+right(r,c)
        no_left = up(r,c)+right(r,c)+down(r,c)
        temp = [no_up, no_down, no_left]
    else:
        temp = up(r,c)+left(r,c),right(r,c)+down(r,c)
        cases.append(temp)
max_cnt = 0
for pairs in zip(case for case in cases):
    temp = set()
    for pair in pairs:
        detected = pair[0]
        for i in (1, len(pair)):
            detected += pair[i]

