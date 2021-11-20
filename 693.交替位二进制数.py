#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        compare = 1
        for each_char in bin(n)[2:]:
            if each_char != str(compare):
                return False
            compare ^= 1
        return True
# @lc code=end

