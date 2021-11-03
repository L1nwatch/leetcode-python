#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        result = 0
        i = j = 0
        while i < len(g) and j < len(s):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j < len(s):
                result += 1
            i += 1
            j += 1
        return result

# @lc code=end

