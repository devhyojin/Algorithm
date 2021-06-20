n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

result = 0

coin.sort(reverse=True)

for i in coin:
    if k == 0: break
    result += k // i
    k %= i

print(result)