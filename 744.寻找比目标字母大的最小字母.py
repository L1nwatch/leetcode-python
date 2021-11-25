#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ord_target = ord(target)
        for letter in letters:
            if ord_target < ord(letter):
                return letter
        return letters[0]
# @lc code=end

