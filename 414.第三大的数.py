#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(nums)

        num_1st, num_2rd, num_3th = nums[0], None, None
        for each_num in nums:
            if each_num > num_1st:
                num_1st, num_2rd, num_3th = each_num, num_1st, num_2rd
        if num_3th is not None:
            return num_3th
        else:
            return num_1st
# @lc code=end
