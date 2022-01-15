#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        length = len(mat)
        for i in range(length):
            answer += mat[i][i]
            if i * 2 != length-1:
                answer += mat[i][length-i-1]
        return answer

# @lc code=end

