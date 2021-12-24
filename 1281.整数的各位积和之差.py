#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        n = [int(x) for x in str(n)]
        return reduce(lambda x, y: x*y, n) - sum(n)
# @lc code=end
