#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = list()
        for i in range(n+1):
            result.append(bin(i)[2:].count("1"))
        return result
# @lc code=end
