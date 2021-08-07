#sol1
def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
    return answer

#sol2
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes,signs))
