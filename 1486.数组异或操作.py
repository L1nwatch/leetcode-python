#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = start
        for i in range(1, n):
            answer ^= start+2*i
        return answer
# @lc code=end
