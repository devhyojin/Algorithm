from sys import stdin

checkPrime = [False, False] + [True]*999
for i in range(2, 1001):
    if checkPrime[i]:
        for j in range(2*i, 1001, i):
            checkPrime[j] = False

T = int(input())
info = list(map(int, stdin.readline().split()))
ans = 0
for i in info:
    if checkPrime[i]:
        ans += 1
print(ans)