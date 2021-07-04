def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

from sys import stdin
n, k = map(int, stdin.readline().split())
left = (factorial(n) // (factorial(n-k)*factorial(k)))%10007
print(left)