#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp_list = [1]
            for j in range(1, i):
                temp_list.append(result[i-1][j-1]+result[i-1][j])
            temp_list.append(1)
            result.append(temp_list)
        return result
# @lc code=end
