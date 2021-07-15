#sol1
from sys import stdin
from itertools import combinations
n, m = map(int, stdin.readline().split())
print('\n'.join(list(map(' '.join, combinations(map(str, range(1,n+1)), m)))))

#sol2 백트랙킹
from sys import stdin

def sol(k):
    if len(progression) == m:
        for i in range(m):
            print(progression[i], end=" ")
        print()
        return
    for i in range(k, n+1):
        if i not in progression:
            progression.append(i)
            sol(i+1)
            progression.pop()

n, m = map(int, stdin.readline().split())
progression = []
sol(1)