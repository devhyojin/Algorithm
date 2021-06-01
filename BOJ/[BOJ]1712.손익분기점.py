from sys import stdin
A, B, C = map(int, stdin.readline().split())
if C-B > 0:
    print(A // (C - B) + 1)
else:
    print(-1)