from sys import stdin


def multiply(a,b):
    answer = [[0,0] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += a[i][k] * b[k][j]
            answer[i][j] %= 1000000007
    return answer

def solution(m,num):
    if num == 1:
        return m
    temp = solution(m, num // 2)
    if num % 2:
        return multiply(multiply(temp,temp), m)
    else:
        return multiply(temp, temp)

n=int(stdin.readline())
matrix = [[1,1],[1,0]]
print(solution(matrix,n)[0][1])