#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def special_sort(self, num: int):
        if num in self.arr2:
            index = self.arr2.index(num)
            return (0, index)
        return (1, num)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        self.arr2 = arr2
        return sorted(arr1, key=lambda x: self.special_sort(x))
# @lc code=end
