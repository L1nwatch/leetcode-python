#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low < high:
            middle = low + (high-low)//2
            if arr[middle] > arr[middle+1]:
                high = middle
            else:
                low = middle + 1
        return low
# @lc code=end
