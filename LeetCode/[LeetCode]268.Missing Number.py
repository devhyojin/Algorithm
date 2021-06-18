#sol1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        for i in range(leng+1):
            if i not in nums:
                return i
```
단순하게 돌면서 없는 게 나오면 return하도록 설정했다.
2725ms 15.5MB..... 기록이 안 좋다.
```

#sol2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        return sum(range(leng+1))- sum(nums)
```
이번엔 합으로 계산해보았다.
128ms 15.5MB
시간은 많이 줄었지만, 메모리는 그대로다.
```

