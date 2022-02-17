#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
# @lc code=end


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index,length):
            nums[i] = 0
        