#sol1
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

#sol2
def solution(participants, completion):
    participants.sort()
    completion.sort()
    failed = tuple(set(participants)-set(completion))
    if failed:
        return failed[0]
    for p, c in zip(participants, completion):
        if p != c:
            return p