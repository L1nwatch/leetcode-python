#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        answer = str()
        for bit in n:
            answer += str(int(bit) ^ 1)
        return int(answer, 2)
# @lc code=end
