from sys import stdin
n = int(stdin.readline())
aliquots = list(map(int, stdin.readline().split()))
print(min(aliquots)*max(aliquots))