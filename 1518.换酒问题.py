#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = empty = numBottles
        while empty >= numExchange:
            exchange = empty // numExchange
            answer += exchange
            empty = exchange + empty % numExchange
        return answer
# @lc code=end
