from sys import stdin

def sol(x, y, z):
    if y == 1:
        return x % z
    val = sol(x, y//2, z)
    if y%2 == 0:
        return val * val % z
    return val * val * a % z
a,b,c = map(int, stdin.readline().split())
print(sol(a,b,c))