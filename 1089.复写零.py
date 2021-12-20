#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        length = len(arr)
        while index < length:
            if arr[index] == 0:
                arr.insert(index,0)
                index += 2
            else:
                index += 1
        while len(arr) > length:
            arr.pop()
        
# @lc code=end

