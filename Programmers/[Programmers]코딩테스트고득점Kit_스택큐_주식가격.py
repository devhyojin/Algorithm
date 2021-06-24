from collections import deque
def solution(prices):
    answer = [0 for _ in prices]
    prices = deque(prices)
    idx = -1
    while prices:
        cur_price = prices.popleft()
        idx += 1
        for price in prices:
            answer[idx] += 1
            if price < cur_price:
                break
    return answer
