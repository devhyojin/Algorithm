# sol1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) == 1:
                return i

# sol2
class Solution:
      def singleNumber(self, nums: List[int]) -> int: 
          only = set(nums)
          return sum(only)*2 -sum(nums)