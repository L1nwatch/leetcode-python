#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        import collections
        counter = collections.Counter(stones)
        for jewel in jewels:
            answer += counter.get(jewel,0)
        return answer
# @lc code=end

