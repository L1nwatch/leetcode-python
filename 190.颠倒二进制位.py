#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_bin = bin(n)[2:].zfill(32)[::-1]
        return int(reverse_bin,2)
# @lc code=end

