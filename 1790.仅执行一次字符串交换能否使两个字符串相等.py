#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        length_s2 = len(s2)
        if length_s1 != length_s2:
            return False
        if s1 == s2:
            return True
        if length_s1 < 2:
            return False
        s1_diff = list()
        s2_diff = list()
        for i in range(length_s1):
            if s1[i] != s2[i]:
                s1_diff.append(s1[i])
                s2_diff.append(s2[i])
                if len(s1_diff) > 2:
                    return False
        if len(s1_diff) < 2:
            return False
        if s1_diff[0] == s2_diff[1] and s1_diff[1] == s2_diff[0]:
            return True
        return False
# @lc code=end

