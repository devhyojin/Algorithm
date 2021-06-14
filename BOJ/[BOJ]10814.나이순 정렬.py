# sol2 (44084KB, 256ms)
from sys import stdin
n = int(stdin.readline())
info = []
for _ in range(n):
    age, name = stdin.readline().split()
    age = int(age)
    info.append((age, name))
info.sort(key=lambda x: x[0])
for a, b in info:
    print(a, b)

# sol2 (50228KB, 256ms)
from sys import stdin
n = int(stdin.readline())
info = [tuple(stdin.readline().split()) for _ in range(n)]
info.sort(key=lambda x: int(x[0]))
for a, b in info:
    print(a, b)