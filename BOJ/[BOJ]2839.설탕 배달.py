from sys import stdin
N = int(stdin.readline())
max_five = N // 5
for i in range(max_five, -1):
    if not (N - 5*i) % 3:
        print(i + (N - 5*i)//3)
        break
