# sol1 (81848KB, 1300ms)
from sys import stdin
n = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(n)]
for number in sorted(numbers):
    print(number)

# sol2 (84820KB, 1076ms)
def counting_sort():
    check = [False] * 2000001
    for i in numbers:
        check[i + 1000000] = True
    for j in range(2000001):
        if check[j]: print(j - 1000000)

from sys import stdin
n = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(n)]
counting_sort()
