M = int(input())
N = int(input())

check_prime = [False, False] + [True]*(N-1)
for i in range(2, int(N**0.6)):
    if check_prime[i]:
        for j in range(2*i, N+1, i):
            check_prime[j] = False
prime_num = [i for i in range(M, N+1) if check_prime[i]]
if len(prime_num):
    print(sum(prime_num))
    print(prime_num[0])
else:
    print(-1)