#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        length = len(bits)
        while index < length:
            if bits[index] == 1:
                index += 2
                continue
            if index == length - 1:
                return True
            if bits[index] == 0:
                index += 1
        return False
# @lc code=end

