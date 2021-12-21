#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counter = Counter(text)
        answer = min([counter.get("b", 0), counter.get("a", 0), counter.get(
            "l", 0)//2, counter.get("o", 0)//2, counter.get("n", 0)])
        return answer
# @lc code=end
