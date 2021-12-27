#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        num = list(str(num))
        for index in range(len(num)):
            if num[index] == "6":
                num[index] = "9"
                break
        return int("".join(num))

# @lc code=end
