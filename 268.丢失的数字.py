#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for each_index in range(len(nums)):
            if each_index != nums[each_index]:
                return each_index
        return len(nums)
# @lc code=end
