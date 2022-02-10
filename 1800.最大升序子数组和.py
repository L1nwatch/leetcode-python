#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = temp_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                temp_sum += nums[i]
            else:
                answer = max(answer,temp_sum)
                temp_sum = nums[i]
        else:
            answer = max(answer,temp_sum)
        return answer
# @lc code=end

