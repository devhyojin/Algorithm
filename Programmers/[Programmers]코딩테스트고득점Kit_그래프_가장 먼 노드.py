from collections import defaultdict, deque
def solution(n, edges):
    graph=[[] for _ in range(n+1)]
    dis = [-1 for _ in range(n+1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    queue = deque([1])
    dis[1] = 0
    while queue:
        cur = queue.popleft()
        for v in graph[cur]:
            if dis[v] == -1:
                queue.append(v)
                dis[v] = dis[cur] + 1
    farthest = max(dis)
    return dis.count(farthest)