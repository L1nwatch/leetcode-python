#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = list()
        answer = 0
        index = 0
        length = len(s)
        while index < length:
            if len(stack) == 0 or s[index] == stack[-1]:
                stack.append(s[index])
                index += 1
            else:
                while index < length and len(stack) > 0 and s[index] != stack[-1]:
                    stack.pop()
                    index += 1
                if len(stack) == 0:
                    answer += 1
        return answer
# @lc code=end

