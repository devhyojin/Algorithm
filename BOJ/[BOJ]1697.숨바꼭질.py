from sys import stdin
from collections import deque

def bfs():
    while distance[k] == -1:
        cur = queue.popleft()
        for dir in (cur - 1, cur + 1, cur * 2):
            if dir < 0 or dir > 100000:
                continue
            if distance[dir] != -1:
                continue
            distance[dir] = distance[cur] + 1
            queue.append(dir)
    return distance[k]

n, k = map(int, stdin.readline().split())
distance = [-1]* 100002
queue = deque()
distance[n] = 0
queue.append(n)
print(bfs())
