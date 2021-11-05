#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # left
                    if i <= 0 or grid[i-1][j] == 0:
                        result += 1
                    # right
                    if i >= len(grid) - 1 or grid[i+1][j] == 0:
                        result += 1
                    # top
                    if j <= 0 or grid[i][j-1] == 0:
                        result += 1
                    # bottom
                    if j >= len(grid[0])-1 or grid[i][j+1] == 0:
                        result += 1
        return result
# @lc code=end
