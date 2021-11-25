#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        pre_1, pre_2 = 0, 0
        for i in range(2, length+1):
            next = min(pre_1+cost[i-1], pre_2+cost[i-2])
            pre_1, pre_2 = next, pre_1
        return next

# @lc code=end
