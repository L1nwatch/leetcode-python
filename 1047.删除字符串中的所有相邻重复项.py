#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

        

# @lc code=end
        import re
        while True:
            output = re.sub(r"([a-z])\1", "", s)
            if output == s:
                break
            s = output
        return s