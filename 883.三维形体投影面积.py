#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        answer = [0, 0, 0]
        for i in range(len(grid)):
            answer[0] += len([x for x in grid[i] if x != 0])
            answer[1] += max(grid[i])
        
        for j in range(len(grid[0])):
            answer[2] += max([grid[x][j] for x in range(len(grid))])

        return sum(answer)
# @lc code=end
