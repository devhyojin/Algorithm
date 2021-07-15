# sol1
from sys import stdin
from itertools import combinations
n, s = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
cnt = 0
for i in range(1, n+1):
    cases = combinations(nums, i)
    for case in cases:
        if sum(case) == s:
            cnt += 1
print(cnt)

# sol2 백트래킹
from sys import stdin
n, s = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
def sol(k, comb_sum):
    global cnt
    if k >= n:
        return
    sol(k+1, comb_sum)
    comb_sum += nums[k]
    if comb_sum == s:
        cnt += 1
    sol(k+1, comb_sum)

cnt = 0
sol(0,0)
print(cnt)