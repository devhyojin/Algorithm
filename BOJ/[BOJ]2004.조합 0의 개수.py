def calc(x, alliquot):
    ans = 0
    while x:
        x //= alliquot
        ans += x
    return ans

from sys import stdin
n, m = map(int, stdin.readline().split())
if not m:
    print(0)
else:
    zero_num = min(calc(n, 2)-calc(n-m, 2)-calc(m, 2), calc(n, 5)-calc(n-m, 5)-calc(m, 5))
    print(zero_num)