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


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1],2)

class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(32):
            answer |= (n & 1) << (31 - i)
            n >>= 1
        return answer
    
class Solution3:
    def reverseBits(self, n: int) -> int:
        answer = 0

        for i in range(32):
            answer |= (n & 1) << (31-i)
            n >>= 1
        return answer