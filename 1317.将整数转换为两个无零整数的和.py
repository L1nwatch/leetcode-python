#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(n-1, 0, -1):
            if "0" not in str(num) and "0" not in str(x := n-num):
                return [num, x]

# @lc code=end
