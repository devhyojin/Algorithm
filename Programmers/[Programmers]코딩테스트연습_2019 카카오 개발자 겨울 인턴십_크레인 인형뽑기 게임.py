#sol1
def solution(board, moves):
    answer = 0
    stack = []
    t_board = [[]]
    for j in range(len(board)):
        col = []
        for i in range(len(board) - 1, -1, -1):
            if board[i][j]:
                col.append(board[i][j])
        t_board.append(col)

    for move in moves:
        if t_board[move]:
            picked = t_board[move].pop()
            if stack and stack[-1] == picked:
                stack.pop()
                answer += 2
            else:
                stack.append(picked)
    return answer

#sol2
def solution(board, moves):
    stack = [0]
    answer = 0
    for move in moves:
        for i in range(len(board)):
            picked = board[i][move-1]
            if picked:
                if stack and stack[-1] == picked:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(picked)
                board[i][move-1] = 0
                break
    return answer