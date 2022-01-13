#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        length = len(arr)
        arr_index = 0
        num = 1
        while arr_index < length:
            if arr[arr_index] == num:
                arr_index += 1
                num += 1
            elif arr[arr_index] != num:
                k -= 1
                if k == 0:
                    return num
                num += 1
        while k-1 != 0:
            k -= 1
            num += 1
        return num
# @lc code=end
