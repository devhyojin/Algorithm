from sys import stdin
input = stdin.readline

n = int(input())
piles = list(map(int, input().split()))
left = n - piles.count(0)
one_cnt = piles.count(1)
turn = 0
while True:
    if one_cnt == left:
        turn += one_cnt
        break

    turn += 1
    if left % 2:
        for i in range(n):
            if piles[i] > 1:
                piles[i] = 1
                one_cnt += 1
                break
    else:
        for i in range(n):
            if piles[i] > 1:
                piles[i] = 0
                left -= 1
                break
if turn % 2:
    print('cubelover')
else:
    print('koosaga')