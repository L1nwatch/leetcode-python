#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def pre(x): return (x+1)//2
        return pre(high)-pre(low-1)

# @lc code=end
