#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        import collections
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        for each_char in count_t.keys():
            if each_char not in count_s or count_s[each_char] != count_t[each_char]:
                return each_char
# @lc code=end
