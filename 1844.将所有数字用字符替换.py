#
# @lc app=leetcode.cn id=1844 lang=python3
#
# [1844] 将所有数字用字符替换
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = list()
        length = len(s)
        for i in range(1,length,2):
            answer.append(s[i-1])
            replace_char = chr(ord(s[i-1])+int(s[i]))
            answer.append(replace_char)
        if length % 2 != 0:
            answer.append(s[-1])
        return "".join(answer)

# @lc code=end

