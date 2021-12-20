#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        candidate = str1[:math.gcd(len(str1), len(str2))]
        if str1+str2 == str2+str1:
            return candidate
        return str()
# @lc code=end
