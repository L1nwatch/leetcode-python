#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for index in range(1, len(s)):
            max_score = max(s[:index].count(
                "0")+s[index:].count("1"), max_score)
        return max_score
# @lc code=end
