#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_x, min_y = m, n
        for a, b in ops:
            min_x = min(a, min_x)
            min_y = min(b, min_y)
        return min_x*min_y

# @lc code=end
