#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_arr = sorted(arr)
        index_map = dict()
        index = 1
        for value in sort_arr:
            if value not in index_map:
                index_map[value] = index
                index += 1

        for index in range(len(arr)):
            arr[index] = index_map[arr[index]]
        return arr
# @lc code=end
