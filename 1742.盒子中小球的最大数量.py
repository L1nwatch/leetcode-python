#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#

# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counter = dict()
        for ball in range(lowLimit,highLimit+1):
            sum_ball = sum([int(x) for x in str(ball)])
            counter[sum_ball] = counter.get(sum_ball, 0) + 1
        max_value = max(counter.values())
        return max_value
# @lc code=end

