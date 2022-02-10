#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        nums = list()
        for i in range(10):
            if str(i) in s:
                nums.append(i)
        if len(nums) > 1:
            return nums[-2]
        else:
            return -1
# @lc code=end

