#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    answer += 2

                    # left
                    next_col = j-1
                    next_row = i
                    next_value = 0
                    if next_col >= 0:
                        next_value = grid[next_row][next_col]
                    answer += max(grid[i][j]-next_value, 0)

                    # right
                    next_col = j+1
                    next_row = i
                    next_value = 0
                    if next_col < len(grid[0]):
                        next_value = grid[next_row][next_col]
                    answer += max(grid[i][j]-next_value, 0)
                    # top
                    next_col = j
                    next_row = i-1
                    next_value = 0
                    if next_row >= 0:
                        next_value = grid[next_row][next_col]
                    answer += max(grid[i][j]-next_value, 0)
                    # bottom
                    next_col = j
                    next_row = i+1
                    next_value = 0
                    if next_row < len(grid):
                        next_value = grid[next_row][next_col]
                    answer += max(grid[i][j]-next_value, 0)
        return answer
# @lc code=end
