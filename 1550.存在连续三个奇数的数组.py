#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length = len(arr)
        if length <= 2:
            return False
        index = 2
        while index < length:
            if arr[index] % 2 == 0:
                index += 3
            elif arr[index-1] % 2 == 0:
                index += 2
            elif arr[index-2] % 2 != 0:
                return True
            else:
                index += 1
        return False

# @lc code=end
