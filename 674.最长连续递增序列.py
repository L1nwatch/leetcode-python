#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        answer = 0
        length = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1]:
                length += 1
            else:
                answer = max(answer, length)
                length = 1

        return max(answer, length)
# @lc code=end
