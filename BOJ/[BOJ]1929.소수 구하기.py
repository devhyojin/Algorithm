M, N = map(int, input().split())

check_prime = [False, False] + [True]*(N-1)
for i in range(2, N+1):
    if check_prime[i]:
        for j in range(2*i, N+1, i):
            check_prime[j]=False

for i in range(M, N+1):
    if check_prime[i]:
        print(i)