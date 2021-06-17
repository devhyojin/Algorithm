from sys import stdin

def dfs(idx, ans):
    global max_ans
    global min_ans

    if idx == n -1:
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans
        return

    for i in range(4):
        temp = ans
        if not oper_num[i]:
            continue
        if i == 0:
            ans += nums[idx+1]
        elif i == 1:
            ans -= nums[idx+1]
        elif i == 2:
            ans *= nums[idx+1]
        else:
            if ans < 0:
                ans = abs(ans) // nums[idx+1]*-1
            else:
                ans //= nums[idx+1]
        oper_num[i] -= 1
        dfs(idx+1, ans)
        oper_num[i] += 1
        ans = temp


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
oper_num = list(map(int, stdin.readline().split()))
max_ans, min_ans = -1 *(1e10), 1e10
dfs(0, nums[0])
print(max_ans)
print(min_ans)