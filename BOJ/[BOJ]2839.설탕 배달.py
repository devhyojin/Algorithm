N = int(input())
ans = 0
for i in range(N//5, -1, -1):
    temp = N - 5 * i
    if not (temp) % 3:
        ans = i + (temp)//3
        break
if ans:
    print(ans)
else:
    print(-1)