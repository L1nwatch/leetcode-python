#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total_sum = 1
        index = 2
        if num == 1:
            return False
        while index ** 2 <= num:
            if num % index == 0:
                total_sum += index
                if index ** 2 != num:
                    total_sum += num / index
            index += 1
        return total_sum == num
# @lc code=end

