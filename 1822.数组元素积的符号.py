#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_num = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negative_num += 1
        return 1 if negative_num % 2 == 0 else -1

# @lc code=end

