from sys import stdin
def sol(k):
    global cnt
    if k == n:
        cnt += 1
        return
    for i in range(n):
        if col_used[i] or upright_used[i+k] or upleft_used[k-i+n-1]:
            continue
        col_used[i] = True
        upright_used[i+k] = True
        upleft_used[k-i+n-1] = True
        sol(k+1)
        col_used[i] = False
        upright_used[i+k] = False
        upleft_used[k-i+n-1] = False



n = int(stdin.readline())
col_used, upright_used, upleft_used = [False]*n, [False]*(2*n+1), [False]*(2*n+1)
cnt = 0
sol(0)
print(cnt)