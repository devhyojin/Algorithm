from itertools import permutations
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True


def solution(numbers):
    ans = 0
    num_list = []
    num_cases = set()
    for i in range(len(numbers)):
        num = int(numbers[i])
        num_list.append(str(num))
        if num > 1:
            num_cases.add(num)

    for j in range(2, len(numbers) + 1):
        temp = list(permutations(num_list, j))
        for t in temp:
            temp_num = int(''.join(t))
            if temp_num > 1:
                num_cases.add(temp_num)

    for case in num_cases:
        if is_prime(case):
            ans += 1
    return ans