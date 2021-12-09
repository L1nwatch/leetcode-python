#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        pre = arr[0]
        index = 1
        length = len(arr)
        asc = True
        while index < length:
            if arr[index] == pre:
                return False
            elif asc and arr[index] > pre:
                pre = arr[index]
                index += 1
            elif asc and arr[index] < pre:
                if index == 1:
                    return False
                asc = False
                pre = arr[index]
                index += 1
            elif not asc and arr[index] > pre:
                return False
            elif not asc and arr[index] < pre:
                pre = arr[index]
                index += 1
        return asc == False
# @lc code=end
