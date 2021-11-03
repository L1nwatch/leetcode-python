#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        index = 0
        length = len(s)
        while index < length:
            if s[index] == " ":
                index += 1
                continue
            else:
                count += 1
                while index < length and s[index] != " ":
                    index += 1
        return count
# @lc code=end
