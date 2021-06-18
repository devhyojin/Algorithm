#sol1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```
set으로 변환 후 길이를 비교해서 풀었습니다.
124ms 20.4MB
```