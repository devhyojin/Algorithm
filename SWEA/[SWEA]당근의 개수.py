from sys import stdin
t = int(stdin.readline())
for tc in range(1,t+1):
    n = int(stdin.readline())
    carrots = list(map(int, stdin.readline().split()))
    max_idx = -1
    max_cnt = -1
    for idx, cnt in enumerate(carrots, start=1):
        if cnt > max_cnt:
            max_idx, max_cnt = idx, cnt
    print(f'#{tc} {max_idx} {max_cnt}')