from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    Q = deque()
    for idx in range(n):
        if not visited[idx]:
            Q.append(idx)
            while Q:
                cur_com = Q.popleft()
                visited[cur_com] = 1
                for other_com in range(n):
                    if cur_com != other_com and computers[cur_com][other_com] and not visited[other_com]:
                        Q.append(other_com)
            answer += 1
    return answer