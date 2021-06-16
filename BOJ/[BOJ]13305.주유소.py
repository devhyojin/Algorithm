from sys import stdin

n = int(stdin.readline())
far = tuple(map(int, stdin.readline().split()))
price = tuple(map(int, stdin.readline().split()))

cost= price[0] * far[0]
before = price[0]
for i in range(1, n - 1):
    if price[i] < before:
        before = price[i]
    cost += before * far[i]
print(cost)
