#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
class Solution:
    def get_area(self, p1: list, p2: list, p3: list) -> float:
        return 0.5 * abs(p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p1[1]*p2[0]-p2[1]*p3[0]-p3[1]*p1[0])

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        import itertools
        return max([self.get_area(x, y, z) for x, y, z in itertools.combinations(points, 3)])
# @lc code=end
