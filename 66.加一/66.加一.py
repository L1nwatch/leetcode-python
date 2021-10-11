#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = str(int("".join([str(i) for i in digits]))+1)
        return [int(i) for i in list(answer)]
# @lc code=end
