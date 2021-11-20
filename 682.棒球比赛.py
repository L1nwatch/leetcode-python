#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = list()
        for each_char in ops:
            if each_char == "+":
                result.append(result[-1]+result[-2])
            elif each_char == "C":
                result.pop()
            elif each_char == "D":
                result.append(2*result[-1])
            else:
                result.append(int(each_char))
        return sum(result)
# @lc code=end

