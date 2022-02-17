#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left <= right:
            answer = numbers[left] + numbers[right]
            if answer == target:
                return [left+1, right+1]
            elif answer > target:
                right -= 1
            elif answer < target:
                left += 1
# @lc code=end

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left_index, right_index = 0, length - 1
        while left_index < right_index:
            temp_sum = numbers[left_index] + numbers[right_index]
            if temp_sum > target:
                right_index -= 1
            elif temp_sum < target:
                left_index += 1
            else:
                return [left_index + 1,right_index + 1]
        return [-1,-1]