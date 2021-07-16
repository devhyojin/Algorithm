from sys import stdin

def sol(k):
    if k == m:
        for i in range(m):
            print(progression[i], end=" ")
        print()
        return
    for i in range(1, n+1):
        progression[k] = i
        sol(k+1)

n, m = map(int, stdin.readline().split())
progression = [0]*m
sol(0)