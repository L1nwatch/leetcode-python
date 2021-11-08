#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = False
        if num < 0:
            flag = True
            num = -num
        elif num == 0:
            return "0"
        result = str()
        while num != 0:
            result = str(num % 7) + result
            num //= 7
        if flag:
            result = "-"+result
        return result
# @lc code=end

