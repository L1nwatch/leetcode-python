#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def count(self, raw_string):
        result = 0
        for char in raw_string:
            if char in ('a','e','i','o','u','A','E','I','O','U'):
                result += 1
        return result

    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        s_half1 = s[:length//2]
        s_half2 = s[length//2:]
        return self.count(s_half1) == self.count(s_half2)
        
# @lc code=end

