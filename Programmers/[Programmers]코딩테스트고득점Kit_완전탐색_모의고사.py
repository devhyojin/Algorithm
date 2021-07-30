def solution(answers):
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0 for _ in range(4)]
    for i in range(len(answers)):
        if answers[i] == st1[i % 5]:
            score[1] += 1
        if answers[i] == st2[i % 8]:
            score[2] += 1
        if answers[i] == st3[i % 10]:
            score[3] += 1
    max_score = max(score)
    answer = []
    for idx, val in enumerate(score):
        if val == max_score:
            answer.append(idx)
    return answer
