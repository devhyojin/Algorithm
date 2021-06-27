from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
def solution(nums):
    stack = [0]
    ans = [-1 for _ in range(n)]
    for i in range(1, n):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        stack.append(i)
    return ans
print(*solution(nums))
