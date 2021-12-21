#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        a = 0
        b = 1
        c = 1
        for _ in range(n-2):
            a, b, c = b, c, a+b+c
        return c
# @lc code=end
