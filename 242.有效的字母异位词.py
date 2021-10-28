#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1, count2 = dict(), dict()
        if len(s) != len(t):
            return False

        for each_index in range(len(s)):
            count1[s[each_index]] = count1.get(s[each_index], 0) + 1
            count2[t[each_index]] = count2.get(t[each_index], 0) + 1

        return count1 == count2
            
# @lc code=end
