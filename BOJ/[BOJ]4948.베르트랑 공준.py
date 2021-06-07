#sol1 33060KB 224ms
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

#sol2  30932KB 116ms
max_n = 123456 * 2
# 홀수만 확인합시당
prime_check = [True]*(max_n//2)
for i in range(3, int(max_n ** 0.5) + 1, 2):
    if prime_check[i//2]:
        x = i ** 2
        for j in range(x//2, max_n//2, i):
            prime_check[j] = False
prime_list = [2] + [(2*i+1) for i in range(1, len(prime_check)) if prime_check[i]]

def Search(num):
    l,r = 0, len(prime_list)-1
    while l <=r:
        m = (l+r)//2
        if prime_list[m] > num:
            r = m-1
        else: l = m+1
    return l
while True:
    N = int(input())
    if not N:
        break
    print(Search(2*N) - Search(N))