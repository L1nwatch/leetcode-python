#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = [float("inf"), -1]
        for i in range(len(points)):
            point_x,point_y = points[i]
            if point_x == x or point_y == y:
                distance = abs(point_x-x) + abs(point_y-y)
                if distance < answer[0]:
                    answer = [distance, i]
        return answer[1]
# @lc code=end

