from sys import stdin
n =int(stdin.readline())
for _ in range(n):
    stack = []
    PS = stdin.readline().rstrip()
    for ps in PS:
        if ps == '(':
            stack.append(ps)
        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')