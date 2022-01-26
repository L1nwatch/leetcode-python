#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
class Solution:
    def sort_func(self, x):
        return (self.counter[x], -x)

    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        self.counter = Counter(nums)
        return sorted(nums, key=self.sort_func)
# @lc code=end
