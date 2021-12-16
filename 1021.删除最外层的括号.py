#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = str()
        stack = list()
        index = 0
        for char in s:
            if char == "(":
                stack.append(char)
                index += 1
            elif char == ")":
                stack.append(char)
                index -= 1
                if index == 0:
                    answer += "".join(stack[1:-1])
                    stack = list()
                    index = 0
        return answer
                    
# @lc code=end

