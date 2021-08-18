from sys import stdin
from collections import deque

# def transfer(line_num,cnt):
#     global cnt_list, visited
#     visited[line_num] = 1
#     if line_num == e_idx:
#         cnt_list.append(cnt)
#         return
#     if cnt == l-1:
#         return
#     for c in connected[line_num]:
#         if not visited[c]:
#             transfer(c,cnt+1)

def find_idx():
    global s_idx, e_idx
    for idx, line in enumerate(lines):
        # 출발, 목적지역의 위치 저장
        if s in line:
            s_idx = idx
        if e in line:
            e_idx = idx
    if s_idx == e_idx:
        return True
    else:
        return False

def bfs():
    print('bfs', s_idx, e_idx)
    queue = deque()
    queue.append(s_idx)
    visited[s_idx] = 1
    while queue:
        x = queue.popleft()
        if x == e_idx:
            return visited[x]-1
        for c in connected[x]:
            if not visited[c]:
                visited[c] = visited[x] + 1
                queue.append(c)
    return -1

n, l = map(int, stdin.readline().split())
s_idx, e_idx = -1, -2
lines = [list(map(int, stdin.readline().split()))[:-1] for _ in range(l)]
s,e = map(int, stdin.readline().split())

if find_idx():
    print(0)
else:
    connected=[[]for _ in range(l)]
    visited=[0 for _ in range(l)]

    for i in range(l-1):
        for j in range(i+1,l):
            if list(set(lines[i])&set(lines[j])):
                connected[i].append(j)
                connected[j].append(i)

    print(bfs())
    #
    # cnt_list = []
    # transfer(s_idx,0)
    # if cnt_list:
    #     print(min(cnt_list))
    # else:
    #     print(-1)





