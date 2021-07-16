#sol1
from sys import stdin
from itertools import combinations as cb
def sol(start):
    global min_diff
    link = list(set(range(n)) - set(start))
    start_sum, link_sum = 0, 0
    for x in range(0, n//2-1):
        for y in range(x+1, n//2):
            start_sum += syn[start[x]][start[y]]
            link_sum += syn[link[x]][link[y]]
    cur_diff = abs(start_sum - link_sum)
    if min_diff > cur_diff:
        min_diff = cur_diff
    return

n = int(stdin.readline())
s = [list(map(int,stdin.readline().split())) for _ in range(n)]
print(i for i in zip(*s))
syn = list([0]*n for _ in range(n))
for i in range(n-1):
    for j in range(i+1, n):
        syn[i][j] = s[i][j]+s[j][i]
start_cases = list(cb(list(range(n)), n//2))
min_diff = 100*10
for start in start_cases:
    sol(start)
print(min_diff)

# sol2 백트랙킹
from sys import stdin

def sol(k, h):
    global min_diff
    if k == n//2:
        link = list(set(range(n)) - set(start))
        start_sum, link_sum = 0, 0
        for x in range(0, n//2-1):
            for y in range(x+1, n//2):
                start_sum += syn[start[x]][start[y]]
                link_sum += syn[link[x]][link[y]]
        cur_diff = abs(start_sum - link_sum)
        if min_diff > cur_diff:
            min_diff = cur_diff
        return
    for i in range(h+1, n):
        if not is_used[i]:
            start[k] = i
            is_used[i] = True
            sol(k+1, i)
            is_used[i] = False


n = int(stdin.readline())
s = [list(map(int,stdin.readline().split())) for _ in range(n)]
syn = list([0]*n for _ in range(n))
for i in range(n-1):
    for j in range(i+1, n):
        syn[i][j] = s[i][j]+s[j][i]
is_used = [False]*n
min_diff = 100*10
start = [-1]*(n//2)
sol(0, 0)
print(min_diff)