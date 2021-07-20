from sys import stdin
from collections import deque
def dfs(s):
    visited[s] = True
    print(s, end=" ")
    sorted_list = sorted(infos[s])
    for i in sorted_list:
        if not visited[i]:
            dfs(i)
def bfs(s):
    while queue:
        c = queue.popleft()
        print(c, end=" ")
        sorted_list = sorted(infos[c])
        for i in sorted_list:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v = map(int, stdin.readline().split())
infos = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    infos[a].append(b)
    infos[b].append(a)


stack = [v]
visited[v] = True
dfs(v)
print()
visited = [False]*(n+1)
visited[v] = True
queue = deque()
queue.append(v)
bfs(v)