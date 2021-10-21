#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        circle_set = set()
        circle_set.add(n)
        while True:
            temp_sum = sum([int(each_char)**2 for each_char in str(n)])
            if temp_sum == 1:
                return True
            if temp_sum in circle_set:
                return False
            circle_set.add(temp_sum)
            n = temp_sum
                
# @lc code=end

