#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        middle_insert = False
        import collections
        count = collections.Counter(s)
        for each_count in count.values():
            if each_count % 2 == 0:
                result += each_count
            else:
                result += each_count - 1
                middle_insert = True
        if middle_insert:
            result += 1
        return result
# @lc code=end
