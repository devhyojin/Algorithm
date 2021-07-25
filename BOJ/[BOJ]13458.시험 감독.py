from sys import stdin
from math import ceil

def sol():
    sub_cnt = 0
    for p in ppl:
        if p <= b:
            continue
        sub_cnt += ceil((p-b)/c)
    return n + sub_cnt

n=int(stdin.readline())
ppl=list(map(int, stdin.readline().split()))
b, c = map(int, stdin.readline().split())

print(sol())