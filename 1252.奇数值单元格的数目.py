#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for j in range(n)] for i in range(m)]
        for ri, ci in indices:
            for j in range(0, n):
                matrix[ri][j] += 1
            for i in range(0, m):
                matrix[i][ci] += 1

        answer = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    answer += 1
        return answer

# @lc code=end
