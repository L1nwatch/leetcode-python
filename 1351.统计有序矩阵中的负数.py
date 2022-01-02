#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(n):
                if grid[i][j] < 0:
                    answer += n-j
                    break
        return answer
# @lc code=end

