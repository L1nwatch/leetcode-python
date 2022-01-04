#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = [(num, index) for index, num in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[0])
        answer = [0] * len(nums)
        count, count_num = 0, nums[0]
        for new_index, num_info in enumerate(nums):
            num, old_index = num_info[0], num_info[1]
            if num != count_num:
                count_num = num
                count = new_index
            answer[old_index] = count
        return answer
# @lc code=end
