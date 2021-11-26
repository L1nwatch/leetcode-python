#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        start_list = list()
        for i in range(rows):
            start_list.append([i, 0])
        for j in range(cols):
            start_list.append([0, j])

        min_rows_cols = min(rows, cols)
        for x, y in start_list:
            for i in range(1, min_rows_cols):
                if x+i < rows and y+i < cols:
                    if matrix[x+i][y+i] != matrix[x][y]:
                        return False
        return True
# @lc code=end
