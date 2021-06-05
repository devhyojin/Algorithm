prime_check = [False, False] + [True]*9999
for i in range(2, 10001):
    if prime_check[i]:
        for j in range(2*i, 10001, i):
            prime_check[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range((N+1)//2,1,-1):
        if prime_check[i] and prime_check[N-i]:
            print(i, N-i)
            break