from sys import stdin

def dfs(s):
    for i in info[s]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

n = int(stdin.readline()) #컴퓨터 수
m = int(stdin.readline()) #연결 쌍 수
info = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    info[a].append(b)
    info[b].append(a)
visited = [False, True] + [False]*(n-1)
dfs(1)
print(visited.count(True)-1)