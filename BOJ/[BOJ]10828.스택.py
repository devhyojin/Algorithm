from sys import stdin
n = int(stdin.readline())
stack = []
for _ in range(n):
    order = stdin.readline().split()
    order_type = order[0]
    if order_type == 'push':
        stack.append(order[1])
    elif order_type == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order_type == 'size':
        print(len(stack))
    elif order_type == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
