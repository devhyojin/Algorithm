from sys import stdin
n = int(stdin.readline())
words = list(set(stdin.readline().rstrip() for _ in range(n)))
words.sort(key=lambda x:(len(x), x))
for i in words:
    print(i)