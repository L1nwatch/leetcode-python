#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for each_char in bin(n)[2:]:
            if each_char == "1":
                count += 1
        return count
# @lc code=end

