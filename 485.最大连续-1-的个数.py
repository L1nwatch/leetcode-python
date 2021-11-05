#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > max_num:
                    max_num = count
            elif nums[i] == 0:
                count = 0
        return max_num
# @lc code=end
