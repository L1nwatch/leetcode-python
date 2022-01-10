#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num_1st, num_2nd = 1, 1
        for num in nums:
            if num > num_1st:
                num_1st, num_2nd = num, max(num_1st, num_2nd)
            elif num > num_2nd:
                num_2nd = num
        return (num_1st-1)*(num_2nd-1)
# @lc code=end
