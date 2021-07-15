#sol1
from sys import stdin
from itertools import permutations
n, m = map(int, stdin.readline().split())
perms = permutations(range(1,n+1), m)
for perm in perms:
    for p in perm:
        print(p, end=" ")
    print()

#sol2 백트랙킹
from sys import stdin

def sol(k):
    if k == m:
        for i in range(m):
            print(progression[i], end=" ")
        print()
        return
    for i in range(1, n+1):
        if not is_used[i]:
            progression[k] = i
            is_used[i] = True
            sol(k+1)
            is_used[i] = False

n, m = map(int, stdin.readline().split())
progression = [0]*m
is_used = [False]*(n+1)
sol(0)