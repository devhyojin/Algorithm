t = int(input())
for tc in range(1,t+1):
    n = int(input())
    nums=list(map(int, input().split()))
    min_num = 10000000000
    min_idx = -1
    for idx,num in enumerate(nums, start=1):
        if min_num > num:
            min_idx, min_num = idx, num
    print(f'#{tc} {min_idx}')