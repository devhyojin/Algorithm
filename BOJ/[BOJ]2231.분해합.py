n = int(input())

for i in range(1, n+1):
    temp = list(map(int, str(i)))
    mother = i + sum(temp)
    if mother == n:
        print(i)
        break
    if i == n:
        print(0)
