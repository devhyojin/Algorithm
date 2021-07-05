def gcd_cal(cur_gcd, num):
    rest = cur_gcd % num
    while rest:
        cur_gcd = num
        num = rest
        rest = cur_gcd % num
    return num

from sys import stdin
n = int(stdin.readline())
nums = sorted([int(stdin.readline()) for _ in range(n)])
gcd = nums[1]-nums[0]
for i in range(2, n):
    gcd = gcd_cal(gcd, nums[i]-nums[i-1])

divisors_list = [gcd]
for i in range(2, int(gcd**0.5)+1):
    if not gcd % i:
        print(i, end = " ")
        if i != gcd//i:
            divisors_list.insert(0, gcd//i)
for divisor in divisors_list:
    print(divisor, end=" ")



