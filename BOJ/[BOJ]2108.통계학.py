from sys import stdin
from collections import Counter
n = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(n)]

def mean(nums):
    return round(sum(nums)/n)

def median(nums):
    nums.sort()
    return (nums[n//2])

def mode(nums):
    num_dic = Counter(nums).most_common()
    if n > 1:
        if num_dic[0][1] == num_dic[1][1]:
            return num_dic[1][0]
        else:
            return num_dic[0][0]
    else:
        return num_dic[0][0]

def scope(nums):
    return max(nums)-min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))