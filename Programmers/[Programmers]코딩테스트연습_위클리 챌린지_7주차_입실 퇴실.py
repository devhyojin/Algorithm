#sol1
def solution(enter, leave):
    results = [{i} for i in range(len(enter))]
    gone = [False for _ in range(len(enter))]

    for left in leave:
        gone[left - 1] = True
        temp_group = set()
        for i in range(enter.index(left)):
            current = enter[i] - 1
            if not gone[current]:
                temp_group.add(current)

        results[left - 1].update(temp_group)
        for t in temp_group:
            results[t].add(left - 1)
            results[t].update(temp_group)

    return [len(result) - 1 for result in results]

#sol2
def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    room = []
    idx = 0
    for left in leave:
        while left not in room:
            room.append(enter[idx])
            idx += 1
        room.remove(left)
        for p in room:
            answer[p-1] += 1
        answer[left-1] += len(room)

    return answer