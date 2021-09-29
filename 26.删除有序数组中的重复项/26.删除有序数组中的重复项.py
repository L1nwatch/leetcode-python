#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = list(set(nums))
        answer.sort()
        length = len(answer)
        for i in range(length):
            nums[i] = answer[i]
        return length
# @lc code=end
        # solution 2
        index_left = 0
        index_right = 1
        while index_right <= len(nums)-1:
            if nums[index_right] == nums[index_left]:
                nums.pop(index_right)
            elif nums[index_right] > nums[index_left]:
                index_left += 1
                index_right += 1
        return index_right
