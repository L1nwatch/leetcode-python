#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = dict()
        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = t[i]
            elif s[i] in char_map and char_map[s[i]] != t[i]:
                return False
        values = char_map.values()
        if len(set(values)) < len(values):
            return False
        return True

# @lc code=end

