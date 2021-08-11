def solution(dartResult):
    bonus_dic = {'S':1, 'D':2, 'T':3}
    score = 0
    scores = []
    for chr in dartResult:
        if chr in bonus_dic:
            score **= bonus_dic[chr]
            scores.append(score)
            score = 0
        elif chr == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif chr == '#':
            scores[-1] *= (-1)
        else: #숫자
            score = score * 10 + int(chr)
    scores.append(score)
    return sum(scores)