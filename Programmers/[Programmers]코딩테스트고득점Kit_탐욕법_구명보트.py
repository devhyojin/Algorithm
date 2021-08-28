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