#sol1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        for i in nums:
            if i == 0:
                zero_num += 1
        for i in range(zero_num):
            nums.remove(0)
            nums.append(0)

#sol2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[0]
        for i in range(zero_num):
            nums.append(0)