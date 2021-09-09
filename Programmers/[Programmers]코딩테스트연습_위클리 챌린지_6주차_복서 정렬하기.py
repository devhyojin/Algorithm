def solution(weights, head2head):
    n = len(weights)
    loser = 'N'*n
    win = {}
    for idx, records in enumerate(head2head, start=1):
        if records == loser:
            win[idx] = [0,0,weights[idx-1]]
        else:
            rate = records.count('W')/(n-records.count('N'))
            wow = 0
            for i in range(n):
                if records[i] == 'W' and weights[idx-1] < weights[i]:
                    wow += 1
            win[idx] = [rate, wow, weights[idx-1]]

    results = [player for player, info in sorted(win.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))]
    return results