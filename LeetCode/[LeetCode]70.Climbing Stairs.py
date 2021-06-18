# sol1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        memo = [0] * (n + 1)

        def sol_backtrack(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]

            memo[i] = sol_backtrack(i + 1, n) + sol_backtrack(i + 2, n)
            return memo[i]

        return sol_backtrack(0, n)
```
아주 오랜만에 memoization을 사용해보았다.
28ms 14.4MB
```