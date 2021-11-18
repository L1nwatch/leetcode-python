#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeat_num = None
        nums = sorted(nums)
        expect_num = 1
        for index in range(len(nums)):
            if not repeat_num and nums[index] == nums[index+1]:
                repeat_num = nums[index]
            if nums[index] == expect_num:
                expect_num += 1
        return [repeat_num, expect_num]
# @lc code=end
