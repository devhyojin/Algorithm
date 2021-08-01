from sys import stdin

def multiplication(mat1,mat2,leng):
    answer = [[0 for _ in range(leng)] for _ in range(leng)]
    for i in range(leng):
        for j in range(leng):
            for k in range(leng):
                answer[i][j] += mat1[i][k] * mat2[k][j]
            answer[i][j] %= 1000
    return answer
n, b = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
temp = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
while b>1:
    copied = matrix[:]
    if b%2:
        temp = multiplication(temp, copied, n)
        b-=1
    else:
        matrix = multiplication(copied, copied, n)
        b//=2
temp = multiplication(temp, matrix, n)

for t in temp:
    for i in range(n):
        print(t[i], end=" ")
    print()