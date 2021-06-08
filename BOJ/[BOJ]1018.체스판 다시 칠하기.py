from sys import stdin
n, m = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(n)]
need_paint = []

for i in range(n - 7):
    for j in range(m - 7):
        a, b = 0, 0
        for j in range(i, i + 8):
            for k in range(j, j + 8):
                if (j+k)%2 == 0:
                    if board[j][k] != 'W':
                        a += 1
                    elif board[j][k] != 'B':
                        b += 1
                else :
                    if board[j][k] != 'B':
                        a += 1
                    elif board[j][k] != 'W':
                        b += 1
        need_paint.append(a)
        need_paint.append(b)

print(min(need_paint))