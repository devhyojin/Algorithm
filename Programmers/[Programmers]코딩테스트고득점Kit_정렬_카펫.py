from math import floor, sqrt
def solution(brown, yellow):
    answer = []
    area = brown + yellow
    mid = int(sqrt(area))

    for i in range(mid, area+1):
        if not area % i:
            temp = brown
            border = 2*i + 2*area//i - 4
            idx = 0
            right = True
            while temp != 0:
                if temp < 0:
                    right = False
                    break
                temp -= (border + (8*idx))
                idx += 1
            if right:
                answer.append(i)
                answer.append(area//i)
                break
    answer.sort(reverse=True)
    return answer