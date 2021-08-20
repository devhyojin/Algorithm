from sys import stdin
for tc in range(1, 11):
    n = int(stdin.readline())
    buildings = list(map(int, stdin.readline().split()))
    answer = 0
    for i in range(2, n-2):
        pivot = buildings[i]
        view = max(0, buildings[i] - max(buildings[i-2:i]+buildings[i+1:i+3]))
        answer += view
    print(f'#{tc} {answer}')