from sys import stdin
import math
A, B, V = map(int, stdin.readline().split())
res = (V-B)/ (A-B)
print(math.ceil(res))
