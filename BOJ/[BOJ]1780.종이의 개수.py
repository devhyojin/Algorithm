from sys import stdin

def counter(sr, sc, leng):
    global answer
    pivot = board[sr][sc]
    if leng == 1:
        answer[pivot+1] += 1
        return
    for i in range(sr, sr+leng):
        for j in range(sc, sc+leng):
            if board[i][j] != pivot:
                l = leng//3
                counter(sr,sc, l)
                counter(sr,sc+l,l)
                counter(sr,sc+2*l,l)
                counter(sr+l,sc, l)
                counter(sr+l,sc+l,l)
                counter(sr+l,sc+2*l,l)
                counter(sr+2*l,sc, l)
                counter(sr+2*l,sc+l,l)
                counter(sr+2*l,sc+2*l,l)
                return
    answer[pivot+1] += 1
    return

n=int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer=[0,0,0]
counter(0,0,n)
for a in answer:
    print(a)