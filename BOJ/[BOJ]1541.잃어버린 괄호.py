from sys import stdin
info = stdin.readline().rstrip().split('-')
ans = sum(map(int, info[0].split('+')))
for i in info[1:]:
    ans -= sum(map(int, i.split('+')))
print(ans)