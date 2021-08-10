def solution(n, stages):
    clear_cnt = [0 for _ in range(n+2)]
    rates = [(0,0) for _ in range(n+2)]
    for stage in stages:
        clear_cnt[stage] += 1
    for idx, val in enumerate(clear_cnt):
        temp_sum = sum(clear_cnt[idx:])
        if temp_sum == 0:
            rates[idx] = (idx,0)
            continue
        rates[idx] = (idx, clear_cnt[idx] / temp_sum)
    rates = rates[1:-1]
    rates.sort(key=lambda x: (-x[1], x[0]))
    answer = [rate[0] for rate in rates]
    return answer