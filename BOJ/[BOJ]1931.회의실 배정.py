from sys import stdin

n = int(stdin.readline())
info = sorted(tuple(tuple(map(int, stdin.readline().split())) for _ in range(n)), key=lambda x: (x[1], x[0]))

ans = before = 0
for start, end in info:
    if start >= before:
        before = end
        ans += 1
print(ans)

