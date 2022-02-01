#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current_high = 0
        for each_gain in gain:
            current_high += each_gain
            highest = max(highest,current_high)
        return highest
# @lc code=end

