#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start
from typing import AnyStr


class Solution:
    def makeGood(self, s: str) -> str:
        stack = list()
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                top = stack[-1]
                if top != char and (top.lower() == char or top.upper() == char):
                    stack.pop()
                else:
                    stack.append(char)
        return "".join(stack)
# @lc code=end
