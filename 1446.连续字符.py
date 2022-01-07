#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        answer = 0
        count = 1
        char = s[0]
        for i in range(1, len(s)):
            if s[i] == char:
                count += 1
            else:
                answer = max(answer, count)
                count = 1
                char = s[i]
        else:
            answer = max(answer, count)
        return answer
# @lc code=end
