from sys import stdin
n = int(stdin.readline())
dots = tuple(map(int, input().split()))
dot_dic = {dot : idx for idx, dot in enumerate(sorted(set(dots)))}
for dot in dots:
    print(dot_dic[dot], end=' ')