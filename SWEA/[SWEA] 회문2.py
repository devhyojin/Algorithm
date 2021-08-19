def check(board_sample):
    for leng in range(100,0,-1):
        for b in board_sample:
            for j in range(0, 101 - leng):
                temp = b[j:j+leng]
                if temp == reversed(temp):
                    return leng

def palin(arr, rev_arr, max_n):
    for i in range(100, 0, -1):
        if max_n > i:
            return max_n
        for j in range(101-i):
            sub

for _ in range(10):
    print(f'#{input()}', end=" ")
    # board = list(list(input()) for _ in range(100))
    # new_board = list(map(list, zip(*board)))
    board=[input() for _ in range(100)]
    answer = 0
    for b in board:
        rev_b = b[::-1]
        answer = palin(b, rev_b, answer)
    print(check(board))