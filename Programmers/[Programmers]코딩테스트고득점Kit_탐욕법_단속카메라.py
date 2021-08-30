def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001
    for i, o in routes:
        if camera < i:
            answer += 1
            camera = o
    return answer