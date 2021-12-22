#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        point1_x, point1_y = coordinates[0]
        point2_x, point2_y = coordinates[1]
        for x, y in coordinates[2:]:
            if (point1_x-x)*(point1_y-point2_y) != (point1_x-point2_x)*(point1_y-y):
                return False
        else:
            return True

# @lc code=end
