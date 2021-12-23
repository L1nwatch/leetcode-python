#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp_grid = list()
        for each_row in grid:
            temp_grid.extend(each_row)
        k = k % len(temp_grid)
        temp_grid = temp_grid[-k:] + temp_grid[:-k]
        answer = list()
        coln = len(grid[0])
        count = 0
        temp_list = list()
        for num in temp_grid:
            temp_list.append(num)
            count += 1
            if count == coln:
                answer.append(temp_list)
                temp_list = list()
                count = 0
        return answer
# @lc code=end
