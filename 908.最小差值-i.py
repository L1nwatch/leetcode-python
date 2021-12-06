#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num, max_num = min(nums), max(nums)
        if max_num - min_num <= 2 * k:
            return 0
        else:
            return max_num - min_num - 2 * k
# @lc code=end
