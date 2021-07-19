from sys import stdin

def checker(r, c):
    bw_cnt, wb_cnt = 0, 0
    for i in range(r,r+8):
        for j in range(c, c+8):
            if i%2:
                if board[i][j] != wb[j]:
                    bw_cnt += 1
                elif board[i][j] != bw[j]:
                    wb_cnt += 1
            else:
                if board[i][j] != bw[j]:
                    bw_cnt += 1
                elif board[i][j] != wb[j]:
                    wb_cnt += 1
    return min(bw_cnt, wb_cnt)


n, m = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(n)]
bw, wb = 'BW'*(m//2), 'WB'*(m//2)
if m%2:
    bw += 'B'
    wb += 'W'

cnt_list = []
for i in range(n-7):
    for j in range(m-7):
        cnt_list.append(checker(i,j))
print(min(cnt_list))
