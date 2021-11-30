#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
class Solution:
    def intersect(self, left1: int, right1: int, left2: int, right2: int) -> bool:
        return min(right1, right2) > max(left1, left2)

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return self.intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and self.intersect(rec1[1], rec1[3], rec2[1], rec2[3])
# @lc code=end
