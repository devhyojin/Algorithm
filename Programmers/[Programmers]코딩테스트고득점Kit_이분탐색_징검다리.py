def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    l,r = 0,distance
    while l <= r:
        mid = (l+r)//2
        min_far = 1000000000
        remove_cnt = 0
        start = 0
        for rock in rocks:
            far = rock - start
            if far < mid:
                remove_cnt += 1
            else:
                start = rock
                min_far = min(min_far, far)
        if remove_cnt > n:
            r = mid -1
        else:
            l = mid + 1
            answer = min_far
    return answer