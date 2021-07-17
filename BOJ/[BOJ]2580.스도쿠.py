from sys import stdin
def fill_sudoku(b):
    if b == len(blanks):
        for row in board:
            print(' '.join(row))
        return
    bi, bj = blanks[b]
    di, dj = bi-(bi%3), bj-(bj%3)

    for i in range(9):
        row_check(i, bi)
        col_check(i, bj)
    sqr_check(di,dj)

    can_num = []
    for i in range(10):
        if not onenine[i]:
            can_num.append(i)
    for num in can_num:
        board[bi][bj] = num
        fill_sudoku(b+1)
        board[bi][bj] = 0
def row_check(x, bx):
    room = board[bx][x]
    if room:
        onenine[room] = True
    return
def col_check(x, bx):
    room = board[x][bx]
    if room:
        onenine[room] = True
    return
def sqr_check(by, bx):
    for i in range(by, by+3):
        for j in range(bx, bx+3):
            room = board[i][j]
            if room:
                onenine[room] = True
    return
board = [list(map(int, stdin.readline().split())) for _ in range(9)]
blanks=[(i,j) for i in range(9) for j in range(9) if board[i][j]==0]
onenine = [True] + [False]*9
fill_sudoku(0)
