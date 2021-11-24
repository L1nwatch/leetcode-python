#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        length = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        while index < length:
            if index == 0:
                left_sum = 0
            else:
                left_sum = left_sum + nums[index-1]
            right_sum = right_sum - nums[index]

            if left_sum == right_sum:
                return index
            else:
                index += 1
        return -1
# @lc code=end
