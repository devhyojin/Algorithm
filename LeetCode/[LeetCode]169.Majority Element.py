#sol1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        one = list(set(nums))
        majority, majority_cnt = 0, 0
        for i in one:
            cnt = nums.count(i)
            if majority_cnt < cnt:
                majority, majority_cnt = i, cnt
        return majority

#sol2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]