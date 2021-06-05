from sys import stdin

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if not distance and r1==r2:
        print(-1)
    elif distance > r1+r2 or max(r1,r2) > min(r1,r2) + distance:
        print(0)
    elif distance == r1+r2 or distance == max(r1,r2) - min(r1,r2):
        print(1)
    else:
        print(2)