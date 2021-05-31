from sys import stdin
n = int(stdin.readline())
ans = 0

def han(m):
    if m//100 + m%10 == 2 * ((m%100)//10):
        return 1
    return 0

if n < 100:
    ans = n
else:
    ans = 99
    if n >= 111:
        for i in range(111, n+1):
            ans += han(i)
print(ans)

