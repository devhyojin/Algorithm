#sol1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
                nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)
```
최대 sum을 반환하기 위해서, 이전에 연속된 수를 합한 sum과 현재 num 중 큰 값을 다시 현재 num에 저장하고
for문을 돌면 결국 최대 sum을 반환할 수 있다.
68ms 15.1MB
```