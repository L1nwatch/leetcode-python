#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(x) for x in str(int("".join([str(x) for x in num]))+k)]
# @lc code=end
