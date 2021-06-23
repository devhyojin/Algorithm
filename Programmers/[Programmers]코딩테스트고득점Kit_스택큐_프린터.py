from collections import deque
#sol1
def solution(priorities, location):
    answer=0
    Q = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    while Q:
        task = Q.popleft()
        #맨 앞의 것을 뽑고도, Q가 빈 상태가 아니거나, Q 안에 더 큰 우선순위가 있다면, 뒤로 보내기
        if Q and task[0] < max(Q)[0]:
            Q.append(task)
        else:
            answer += 1
            if task[1] == location:
                break
    return answer

#sol2
'''
all함수는 반복 가능한 자료형의 모든 요소가 True일 때 True를 반환하고,
any함수는 반복 가능한 자료형 중 하나의 요소라도 True라면 True를 반환한다. 
'''
def solution(priorities, location):
    answer=0
    Q = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    while Q:
        task = Q.popleft()
        if any(task[1] < q[1] for q in Q):
            Q.append(task)
        else:
            answer += 1
            if task[0] == location:
                break
    return answer


