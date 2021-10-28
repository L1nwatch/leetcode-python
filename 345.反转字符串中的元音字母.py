#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while s[left].lower() not in ("a", "e", "i", "o", "u") and left < right:
                left += 1
            while s[right].lower() not in ("a", "e", "i", "o", "u") and left < right:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
        return "".join(s)

# @lc code=end
