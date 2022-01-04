#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        s.sort()
        answer = list()
        while len(s) > 0:
            # step1
            char = s.pop(0)
            answer.append(char)

            # step2 + step3
            index = 0
            while index < len(s):
                if s[index] != char:
                    char = s.pop(index)
                    answer.append(char)
                else:
                    index += 1

            # step4
            if len(s) > 0:
                char = s.pop()
                answer.append(char)

            # step5 + step6
            for index in range(len(s)-1, -1, -1):
                if s[index] != char:
                    char = s.pop(index)
                    answer.append(char)
        return "".join(answer)

# @lc code=end
