#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        if duration == 0:
            return 0
        for i in range(len(timeSeries)-1):
            result += min(timeSeries[i+1]-timeSeries[i],duration)
        return result + duration
# @lc code=end

