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
