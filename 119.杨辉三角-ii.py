#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        result_list = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            temp_result = [1]
            for j in range(1, i):
                temp_result.append(result_list[i-1][j-1]+result_list[i-1][j])
            temp_result.append(1)
            result_list.append(temp_result)
        return result_list[rowIndex]
# @lc code=end
