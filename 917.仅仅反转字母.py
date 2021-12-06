#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            elif s[left].isalpha():
                right -= 1
            elif s[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)
# @lc code=end
