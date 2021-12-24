#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for index in range(len(points)-1):
            x1, y1 = points[index]
            x2, y2 = points[index+1]
            minus_x = abs(x1-x2)
            minus_y = abs(y1-y2)
            answer += max(minus_x, minus_y)
        return answer
# @lc code=end
