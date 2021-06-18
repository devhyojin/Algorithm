# sol1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        for price in prices[1:]:
            temp = price - min_price
            if temp < 0:
                min_price = price
            elif temp >  max_profit:
                max_profit = temp
        return max_profit
```
최소값과 최대이윤값을 조건에 따라 계속 갱신시켜서 답을 구했다.
932ms 25.1MB
```