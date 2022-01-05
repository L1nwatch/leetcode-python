#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row_nums = set()
        max_col_nums = set()
        for row in range(len(matrix)):
            min_row_nums.add(min(matrix[row]))
        for col in range(len(matrix[0])):
            max_col_nums.add(max([x[col] for x in matrix]))
        return list(max_col_nums.intersection(min_row_nums))
# @lc code=end

