from sys import stdin
n = int(stdin.readline())
numbers = [0]*10001
for _ in range(n):
    numbers[int(stdin.readline())] += 1
for i in range(1, 10001):
    for j in range(numbers[i]):
        print(i)