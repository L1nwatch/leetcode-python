#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        for i, num in enumerate(nums):
            left_element = length - i
            if num >= left_element:
                if i >= 1 and nums[i-1] < left_element:
                    return left_element
                elif i < 1:
                    return left_element
        return -1
# @lc code=end
