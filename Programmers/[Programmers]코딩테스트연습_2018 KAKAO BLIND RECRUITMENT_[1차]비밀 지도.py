# sol1
def solution(n, arr1, arr2):
    board = []
    for code1, code2 in zip(arr1, arr2):
        decode1, decode2 = bin(code1)[2:].zfill(n), bin(code2)[2:].zfill(n)
        temp = ''
        for num1, num2 in zip(decode1, decode2):
            if int(num1) + int(num2) == 0:
                temp += ' '
            else:
                temp += '#'
        board.append(temp)
    return board

#sol2
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = bin(i|j)[2:] #i|j 했을 때 i와 j를 이진수로 놓고 비트연산자 처리한 값의 십진수 값이 결과로 나온다.
        a12=a12.zfill(n)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer