def solution(given):
    leng = len(given)
    answers = []
    if len(given) == 1:
        return 1

    for gap in range(1, leng // 2 + 1):
        cnt = 1
        result = ""
        pivot = given[:gap]
        for i in range(gap, leng, gap):
            if given[i:i + gap] == pivot:
                cnt += 1
                continue
            if cnt > 1:
                result += str(cnt)
            result += pivot
            pivot = given[i:i + gap]
            cnt = 1

        if cnt > 1:
            result += str(cnt)
        result += pivot
        answers.append(len(result))
    return min(answers)