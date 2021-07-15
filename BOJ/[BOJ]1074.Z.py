from sys import stdin


def sol(i,j,k):
    if i == 0:
        return 0
    half = 2 ** (i - 1)
    if j < half and k < half:
        return sol(i-1, j, k)
    elif j < half and k >= half:
        return  half**2 + sol(i-1, j, k - half)
    elif j >= half and k < half:
        return 2*(half**2) + sol(i-1, j-half, k)
    else:
        return 3*(half**2) + sol(i-1, j-half, k-half)

n,r,c = map(int, stdin.readline().split())
print(sol(n,r,c))