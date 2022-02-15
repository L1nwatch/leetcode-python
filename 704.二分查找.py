#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            middle = low + (high-low)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle
            elif nums[middle] < target:
                low = middle + 1
        return -1
# @lc code=end

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            middle = low + (high - low)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle
            elif nums[middle] < target:
                low = middle + 1
        return -1