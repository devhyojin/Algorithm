from sys import stdin
n = int(stdin.readline())
pac = 1
for i in range(1, n+1):
    pac *= i
pac, ans = str(pac), 0
for j in range(len(pac)-1, -1, -1):
    if pac[j] != '0':
        print(len(pac)-1-j)
        break