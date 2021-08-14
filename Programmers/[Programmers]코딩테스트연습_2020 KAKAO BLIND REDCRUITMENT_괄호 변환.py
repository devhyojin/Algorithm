bracket_dic = {'(':')', ')':'('}

#균형잡힌 괄호 문자열 u,v로 분리시키기
def divide(given):
    temp_u, temp_v = '', ''
    for i in range(len(given)):
        temp_u = given[:i+1]
        if temp_u.count('(') == temp_u.count(')'):
            temp_v = given[i+1:]
            break
    return temp_u, temp_v

#올바른~체크
def is_right(given):
    stack=[]
    for g in given:
        if g == '(':
            stack.append('(')
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(')')
    if stack:
        return False
    else:
        return True

def solution(v):
    answer=""
    while v:
        u, v = divide(v)
        if is_right(u): #u가 올바른~이라면 v에 대해 1단계부터 재수행
            answer += u
        else: #u가 올바른~이 아닐 때 거치는 과정
            temp=""
            for bracket in u:
                temp += bracket_dic[bracket]
            answer += '('+ solution(v) +')' + temp[1:-1]
            break
    return answer