#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = temp_sum = sum(nums[:k])
        length = len(nums)

        for i in range(k, length):
            temp_sum = temp_sum - nums[i-k]+nums[i]
            max_sum = max(max_sum, temp_sum)
        return max_sum/k
# @lc code=end
        max_avg = None
        for i in range(len(nums)-k+1):
            temp_avg = sum(nums[i:i+k])/k
            if max_avg:
                max_avg = max(temp_avg, max_avg)
            else:
                max_avg = temp_avg
        return max_avg
