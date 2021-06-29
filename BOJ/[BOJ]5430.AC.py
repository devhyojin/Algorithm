from sys import stdin
from collections import deque
def calc(operators, n, nums):
    flag = False
    for operator in operators:
        if operator == 'R':
            flag = not flag
        else:
            if not nums:
                return 'error'
            if flag:
                nums.pop()
            else:
                nums.popleft()

    if flag:
        nums.reverse()
    return '[' +','.join(nums) + ']'

t = int(stdin.readline())
for _ in range(t):
    p_func, n, nums = stdin.readline().rstrip(), int(stdin.readline()), stdin.readline()[1:-2].split(',')
    if n:
        nums = deque(nums)
    else:
        nums = deque()
    print(calc(p_func, n, nums))
