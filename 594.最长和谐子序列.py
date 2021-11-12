#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_count = 0
        for i in range(len(nums)):
            temp_count = 0
            for j in range(i, len(nums)):
                if abs(nums[j]-nums[i]) == 1:
                    temp_count += 1
            max_count = max(temp_count, max_count)
        return max_count
# @lc code=end
