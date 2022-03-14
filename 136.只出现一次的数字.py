#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
# @lc code=end
        data = nums[0]
        for each_data in nums[1:]:
            data ^= each_data
        return data

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for i in range(1,len(nums)):
            answer ^= nums[i]
        return answer

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for i in range(1,len(nums)):
            answer ^= nums[i]
        return answer