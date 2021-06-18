#sol1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        for i in range(leng-1):
            for j in range(i+1, leng):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
48 ms 14.2MB의 결과가 나왔다.
```

#sol2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, val in enumerate(nums):
            remaining = target - val

            if remaining in check:
                return [check[remaining]], i]
            else:
                check[val] = i
```
반복문을 돌 때 index값과 value를 동시 에 반환하는  enumerate를 사용해서 풀어보았다.
44ms 14.3MB의 결과가 나왔다.
```