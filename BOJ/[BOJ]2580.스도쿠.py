import sys

def find_candidates(r, c):
    candidates = set(range(1,10))
    #해당 행에 존재하는 것은 후보군에서 제외한다.
    candidates -= set(board[r])
    #해당 열에 존재하는 것은 후보군에서 제외한다.
    col_nums = set()
    for i in range(9):
        col_nums.add(board[i][c])
    candidates -= col_nums
    #해당 사각형에 존재하는 것은 후보군에서 제외한다.
    sqr_nums = set()
    sqr_r, sqr_c = r//3*3, c//3*3
    for i in range(sqr_r,sqr_r+3):
        for j in range(sqr_c, sqr_c+3):
            sqr_nums.add(board[i][j])
    candidates -= sqr_nums
    return tuple(candidates)

def fill_sudoku(b):
    if b == len(blanks):
        [print(*row) for row in board]
        sys.exit()
    br, bc = blanks[b]
    candidates = find_candidates(br, bc)
    for can in candidates:
        board[br][bc] = can
        fill_sudoku(b+1)
        board[br][bc] = 0

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blanks=[(i,j) for i in range(9) for j in range(9) if board[i][j]==0]

fill_sudoku(0)
