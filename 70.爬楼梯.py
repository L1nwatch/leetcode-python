#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a+b
        return b

# @lc code=end
