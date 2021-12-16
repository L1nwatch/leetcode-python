#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False
        target = sum_arr / 3
        cur_sum = 0
        index = 0
        while index < len(arr):
            cur_sum += arr[index]
            if cur_sum == target:
                break
            index += 1
        if cur_sum != target:
            return False
        for j in range(index+1, len(arr)-1):
            cur_sum += arr[j]
            if cur_sum == target * 2:
                return True
        return False
# @lc code=end
