import heapq
def solution(jobs):
    jobs.sort()
    start, end = -1, jobs[0][0]
    cnt, answer = 0,0
    leng = len(jobs)
    wait = []

    while cnt < leng:
        for arrived, runtime in jobs:
            #지금 수행하고 있는 작업 중, 요청되는 job이 있다면
            if start < arrived <= end:
                heapq.heappush(wait, (runtime, arrived))
        #대기리스트에 job이 있다면
        if wait:
            runtime, arrived = heapq.heappop(wait)
            cnt += 1
            #이전 작업이 끝난 시간부터, 새로운 job 가동
            start = end
            end += runtime
            answer += end - arrived
        else:
            end += 1
    return answer//leng
