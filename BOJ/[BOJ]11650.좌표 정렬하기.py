from sys import stdin
n = int(stdin.readline())
dots = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
sorted_dots = sorted(dots, key=lambda x: (x[0], x[1]))
for sorted_dot in sorted_dots:
    a, b = sorted_dot
    print(a, b)