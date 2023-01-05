#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        for i in range(1,len(nums)):
            if nums[i] + nums[i-1] > nums[i]:
                nums[i] += nums[i-1]
            if nums[i] > max_value:
                max_value = nums[i]
        return max_value
# @lc code=end

