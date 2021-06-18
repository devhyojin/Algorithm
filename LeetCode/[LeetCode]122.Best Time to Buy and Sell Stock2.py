# 판매한 당일이라도 구매할 수 있으므로 최대 이익은 가능한 모든 이익의 합이다. 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_sum = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                profit_sum += profit
        return profit_sum