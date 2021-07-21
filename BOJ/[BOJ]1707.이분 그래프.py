from sys import stdin
from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        c = queue.popleft()
        for i in info[c]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -visited[c]
            elif visited[i] == visited[c]:
                return True
    return False

k = int(stdin.readline())
for _ in range(k):
    v, e = map(int, stdin.readline().split())
    info = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    ans = 'YES'
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        info[a].append(b)
        info[b].append(a)
    for i in range(1,v+1):
        if not visited[i]:
            if bfs(i):
                ans = 'NO'
                break
    print(ans)
