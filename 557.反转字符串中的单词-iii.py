#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        result = [x[::-1] for x in s.split(" ")]
        return " ".join(result)
# @lc code=end


class Solution:
    def reverseWords(self, s: str) -> str:
        answer = list()
        words = s.split(" ")
        for word in words:
            answer.append(word[::-1])
        return " ".join(answer)