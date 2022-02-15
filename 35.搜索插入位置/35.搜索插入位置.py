#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low < high - 1:
            index = (low+high)//2
            middle = nums[index]
            if middle == target:
                return index
            elif middle > target:
                high = index
            elif middle < target:
                low = index
        if nums[high] >= target > nums[low]:
            return high
        elif target <= nums[low]:
            return low
        elif target > nums[high]:
            return high + 1
# @lc code=end

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while low <= high:
            middle = low + (high-low)//2
            num = nums[middle]
            if num == target:
                return middle
            elif num > target:
                high = middle - 1
            elif num < target:
                low = middle + 1
        return low