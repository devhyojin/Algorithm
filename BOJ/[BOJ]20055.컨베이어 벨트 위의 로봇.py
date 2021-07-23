#sol1
from sys import stdin

def sol():
    s, e = 0, n - 1
    leng = 2 * n
    ans = 0
    while True:
        ans += 1
        s, e = (s - 1) % leng, (e - 1) % leng
        if belts[e][1]:
            belts[e][1] = 0
        for i in range(e-1, e-n, -1):
            cur, next = i, i+1
            if belts[cur][1] and not belts[next][1] and belts[next][0]:
                belts[cur][1] = 0
                belts[next][0] -= 1
                if next != e:
                    belts[next][1] = 1
        if belts[s][0] and not belts[s][1]:
            belts[s][0] -= 1
            belts[s][1] = 1

        zero = 0
        for belt in belts:
            if belt[0] == 0:
                zero += 1
        if zero >= k:
            return ans

n,k=map(int, stdin.readline().split())
belts = list(map(int, stdin.readline().split()))
for i in range(2*n):
    belts[i] = [belts[i], 0]
print(sol())



#sol2
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
belts = deque(list(map(int, stdin.readline().split())))
robots = deque([0]*n)
ans = 0
while True:
    ans += 1
    belts.rotate(1)
    robots.rotate(1)
    robots[n-1] = 0
    if sum(robots):
        for i in range(n-2,-1,-1):
            cur, next = i, i+1
            if robots[cur] and not robots[next] and belts[next]:
                robots[cur] = 0
                robots[next] = 1
                belts[next] -= 1
        robots[n-1] = 0
    if not robots[0] and belts[0]:
        robots[0] = 1
        belts[0] -= 1
    if belts.count(0) >= k:
        break
print(ans)