#sol1
def solution(people, limit):
    answer = 0
    people.sort()
    s, l = 0, len(people)-1
    while s <= l:
        answer += 1
        temp = people[s] + people[l]
        if temp <= limit:
            s += 1
        l -= 1
    return answer

#sol2
from collections import deque

def solution(people, limit):
    answer = 0
    people=deque(sorted(people, reverse=True))
    while people:
        answer += 1
        left = limit - people.popleft()
        if people and left >= people[-1]:
            people.pop()
    return answer