#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = str()
        while columnNumber > 0:
            columnNumber -= 1
            extra = columnNumber % 26
            answer = chr(ord("A")+extra) + answer
            columnNumber = columnNumber // 26
        return answer
# @lc code=end
