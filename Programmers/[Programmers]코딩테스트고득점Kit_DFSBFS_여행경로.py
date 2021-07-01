from collections import defaultdict
def solution(tickets):
    tickets.sort(reverse=True)
    answer, stack, path = [], ['ICN'], defaultdict(list)
    for start, end in tickets:
        path[start].append(end)
    while stack:
        cur_airport = stack[-1]
        if cur_airport not in path or not path[cur_airport]:
            answer.append(stack.pop())
        else:
            stack.append(path[cur_airport].pop())
    answer.reverse()
    return answer