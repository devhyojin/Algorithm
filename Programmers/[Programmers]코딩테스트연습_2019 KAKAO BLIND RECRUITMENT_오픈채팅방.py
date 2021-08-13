# sol1
def solution(records):
    answer = []
    user_dic = {}
    for record in records:
        temp = list(record.split())
        if temp[0] == 'Enter' or temp[0] == 'Change':
            user_dic[temp[1]] = temp[2]

    for record in records:
        temp = list(record.split())
        if temp[0] == 'Enter':
            answer.append(user_dic[temp[1]] + '님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(user_dic[temp[1]] + '님이 나갔습니다.')
    return answer

# sol2
def solution(records):
    answer = []
    user_dic = {}
    message = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for record in records:
        splited = record.split()
        if splited[0] in ('Enter', 'Change'):
            user_dic[splited[1]] = splited[2]

    for record in records:
        if record.split()[0] == 'Change':
            continue
        answer.append(user_dic[record.split()[1]] + message[record.split()[0]])

    return answer