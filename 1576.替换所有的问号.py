#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        import string
        answer = list()
        length = len(s)
        for i in range(length):
            if s[i] != "?":
                answer.append(s[i])
            else:
                black_char = set()
                if i > 0:
                    black_char.add(s[i-1])
                    black_char.add(answer[-1])
                if i < length - 1:
                    black_char.add(s[i+1])
                for char in string.ascii_lowercase:
                    if char not in black_char:
                        answer.append(char)
                        break
        return "".join(answer)
# @lc code=end
