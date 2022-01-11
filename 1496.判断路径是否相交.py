#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current_point = (0, 0)
        point_set = {current_point}
        for char in path:
            if char == "N":
                current_point = (current_point[0], current_point[1]+1)
            elif char == "S":
                current_point = (current_point[0], current_point[1]-1)
            elif char == "E":
                current_point = (current_point[0]-1, current_point[1])
            elif char == "W":
                current_point = (current_point[0]+1, current_point[1])
            if current_point in point_set:
                return True
            else:
                point_set.add(current_point)
        return False
# @lc code=end
