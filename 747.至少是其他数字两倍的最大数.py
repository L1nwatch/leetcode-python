#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        if all([max_num >= 2*num for num in nums if max_num != num]):
            return nums.index(max_num)
        return -1
# @lc code=end
