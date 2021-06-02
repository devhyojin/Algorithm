from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    H, W, N = map(int, stdin.readline().split())
    if N % H == 0:
        print((H)*100 + (N//H))
    else:
        print((N%H)*100 + (N//H + 1))

