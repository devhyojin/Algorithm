from sys import stdin

def check(sr, sc, l):
    if l == 1:
        return board[sr][sc]
    l//=2
    temp = ''
    temp += check(sr, sc, l)
    temp += check(sr, sc+l, l)
    temp += check(sr+l, sc, l)
    temp += check(sr+l, sc+l, l)

    if temp == '1111':
        return '1'
    elif temp == '0000':
        return '0'
    else:
        return '('+temp+')'

n=int(stdin.readline())
board=[stdin.readline().rstrip() for _ in range(n)]
print(check(0,0,n))