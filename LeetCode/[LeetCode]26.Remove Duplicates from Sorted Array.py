#sol1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[a] = nums[i+1]
                a += 1
        return a
```
새로운 배열을 만들지 않고, 중복되는 수를 없앤 후 그 길이를 반환해야하는 문제였다.
nums가 빈 배열일 때 조건문처리를 넣으면 84ms 15.5MB 넣지 않으면 80ms 16MB가 나온다.
```