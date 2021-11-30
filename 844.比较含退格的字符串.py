#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = list(), list()

        for string, stack in zip([s, t], [stack1, stack2]):
            for char in string:
                if char == "#":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(char)

        return stack1 == stack2


# @lc code=end
