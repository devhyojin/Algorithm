max_n = 123456 * 2
prime_check = [False, False] + [True] * (max_n - 1)
for i in range(2, int(max_n ** 0.5) + 1):
    if prime_check[i]:
        for j in range(2 * i, max_n + 1, i):
            prime_check[j] = False
while True:
    N = int(input())
    if not N:
        break
    print(prime_check[N+1:2*N+1].count(True))