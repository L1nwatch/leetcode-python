#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if n >= i:
                count += 1
                n -= i
            else:
                break
        return count

# @lc code=end
