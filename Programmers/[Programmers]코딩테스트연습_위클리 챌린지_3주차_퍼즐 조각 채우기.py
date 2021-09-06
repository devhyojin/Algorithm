import copy


def dfs(graph, r, c, position, n, num):
    dr = (0, -1, 0, 1)
    dc = (-1, 0, 1, 0)

    ret = [position]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if graph[nr][nc] == num:
            graph[nr][nc] = 2
            ret += dfs(graph, nr, nc, [position[0] + dr[i], position[1] + dc[i]], n, num)

    return ret


def rotate(lst):
    n = len(lst)

    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n - 1 - i] = lst[i][j]

    return ret


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    game_board_copy = copy.deepcopy(game_board)

    block = []

    for i in range(n):
        for j in range(n):
            # 탐색하지 않은 빈 공간을 찾아
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                # block에 빈 공간 모양(result[1:]) 담기
                result = dfs(game_board_copy, i, j, [0, 0], n, 0)[1:]
                block.append(result)
    print(block)
    for r in range(4):
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(table_rotate_copy, i, j, [0, 0], n, 1)[1:]
                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result) + 1)

                        table = copy.deepcopy(table_rotate_copy)

                    else:
                        table_rotate_copy = copy.deepcopy(table)
    return answer

[[[0, 1], [1, 1], [2, 1], [2, 2]], [[1, 0]], [[0, 1], [1, 0]], [[1, 0], [1, -1], [1, 1]], [[1, 0], [1, -1]], []]