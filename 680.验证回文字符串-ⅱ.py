#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        count = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                count += 1
                right -= 1
        if count <= 1:
            return True
        
        left, right = 0, len(s)-1
        count = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                count += 1
                left += 1
        return count <= 1
# @lc code=end
