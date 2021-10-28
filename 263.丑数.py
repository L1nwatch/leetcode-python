#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for each_num in [2, 3, 5]:
            while n % each_num == 0:
                n /= each_num
        return n == 1
# @lc code=end
