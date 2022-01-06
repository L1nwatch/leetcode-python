#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i = 1
        while i < 10**4:
            temp_sum = i
            for num in nums:
                temp_sum += num
                if temp_sum < 1:
                    i += abs(temp_sum) + 1
                    break
            else:
                return i
# @lc code=end
