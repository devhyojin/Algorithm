#sol1
def calculator(n):
    if n >= 90:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 70:
        return 'C'
    if n >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    for j in range(len(scores)):
        self_score = scores[j][j]
        sum_score = 0
        max_score, min_score = 0, 1000
        max_cnt, min_cnt = 0, 0
        mean = 0
        leng = len(scores)
        for i in range(leng):
            temp = scores[i][j]
            sum_score += temp
            if max_score < temp:
                max_score = temp
                max_cnt = 1
            elif max_score == temp:
                max_cnt += 1
            if min_score > temp:
                min_score = temp
                min_cnt = 1
            elif min_score == temp:
                min_cnt += 1
        if max_cnt == 1 and max_score == self_score:
            sum_score -= max_score
            leng -= 1
        if min_cnt== 1 and min_score == self_score:
            sum_score -= min_score
            leng -= 1
        answer += calculator(sum_score/leng)
    return answer


#sol2
def solution(scores) :
    avgs=[]
    score_list =[[score[j] for score in scores] for j in range(len(scores))]

    for idx,val in enumerate(score_list):
        avg = sum(val)
        num = len(val)
        if val[idx] == max(val) or val[idx] == min(val):
            if val.count(val[idx]) == 1 :
                avg -= val[idx]
                num -= 1
        avgs.append(avg/num)

    return "".join([avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs])