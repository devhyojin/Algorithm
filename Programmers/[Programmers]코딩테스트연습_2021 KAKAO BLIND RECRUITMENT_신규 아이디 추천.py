def solution(new_id):
    new_id = new_id.lower() #1단계
    ans_id = ''
    for chr in new_id: #2단계
        if chr.isalnum() or chr in '-_.':
            ans_id += chr
    while '..' in ans_id:#3단계
        ans_id = ans_id.replace('..','.')
    if ans_id and ans_id[0] == '.':#4단계
        ans_id = ans_id[1:]
    if ans_id and ans_id[-1] =='.':
        ans_id = ans_id[:-1]
    if ans_id == '': #5단계
        ans_id= 'a'
    if len(ans_id) > 15: #6단계
        if ans_id[14] == '.':
            ans_id = ans_id[:14]
        else:
            ans_id = ans_id[:15]
    if len(ans_id) < 3: #7단계
        ans_id = ans_id + ans_id[-1] * (3-len(ans_id))
    return ans_id