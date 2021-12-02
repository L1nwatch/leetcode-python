#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = list()
        for j in range(len(matrix[0])):
            new_list = list()
            for i in range(len(matrix)):        
                new_list.append(matrix[i][j])
            answer.append(new_list)
        return answer
# @lc code=end
