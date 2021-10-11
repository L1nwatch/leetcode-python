#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=startaaa
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip() 
        return len(s) - s.rfind(" ") -1
# @lc code=end

