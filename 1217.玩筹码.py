#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        set_position = set(position)
        if len(set_position) == 1:
            return 0
        import sys
        min_price = sys.maxsize
        for each_core in set_position:
            price = 0
            for each_position in position:
                price += 1 if abs(each_position-each_core) % 2 != 0 else 0
            min_price = min(price, min_price)
        return min_price
# @lc code=end
