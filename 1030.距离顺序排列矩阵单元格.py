#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        answer = list()
        for i in range(rows):
            for j in range(cols):
                answer.append(([i, j], abs(i-rCenter)+abs(j-cCenter)))
        answer.sort(key=lambda x: x[1])
        return [x[0] for x in answer]
# @lc code=end
