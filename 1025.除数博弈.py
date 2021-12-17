#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
class Solution:
    def divisorGame(self, n: int) -> bool:
        f = dict()
        f[1] = False
        f[2] = True
        for i in range(3, n+1):
            f[i] = False
            for j in range(1, i):
                if i % j == 0 and f[i-j] is False:
                    f[i] = True
                    break
        return f[n]
# @lc code=end
