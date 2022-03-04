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
    

class Solution:
    def reverseWords(self, s: str) -> str:
        answer = str()
        length = len(s)
        i = 0
        while i < length:
            begin = i
            while i < length and s[i] != " ":
                i += 1
            for j in range(i-1,begin-1,-1):
                answer += s[j]
            while i < length and s[i] == " ":
                i += 1
                answer += " "
        return answer