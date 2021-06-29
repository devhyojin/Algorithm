from sys import stdin
from collections import deque

queue = deque()
n = int(stdin.readline())
for _ in range(n):
    order = stdin.readline().split()
    operator = order[0]
    if operator == 'push':
        queue.append(order[1])
    elif operator == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif operator == 'size':
        print(len(queue))
    elif operator == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif operator == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)