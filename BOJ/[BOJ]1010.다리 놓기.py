from sys import stdin
from math import factorial
t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    print(factorial(m) // (factorial(n)*factorial(m-n)))