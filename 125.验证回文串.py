#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        length = len(s) - 1
        left, right = 0, len(s) - 1
        while left <= length and left <= right and not s[left].isalpha() and not s[left].isalnum():
            left += 1
        while right >= 0 and right >= left and not s[right].isalpha() and not s[right].isalnum():
            right -= 1
        while left <= right:
            if s[left].lower() != s[right].lower():
                result = False
                break
            left += 1
            right -= 1
            while left <= length and left <= right and not s[left].isalpha() and not s[left].isalnum():
                left += 1
            while right >= 0 and right >= left and not s[right].isalpha() and not s[right].isalnum():
                right -= 1

        return result
# @lc code=end
