#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def get_next_num(self, raw_mat):
        for i in range(len(raw_mat)):
            for j in range(len(raw_mat[0])):
                yield raw_mat[i][j]

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        mat_iter = self.get_next_num(mat)
        result = list()
        for i in range(r):
            temp_row = list()
            for j in range(c):
                temp_row.append(next(mat_iter))
            result.append(temp_row)
        return result
# @lc code=end
