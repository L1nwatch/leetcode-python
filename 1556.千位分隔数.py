#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        answer = str()
        count = 0
        for char in str(n)[::-1]:
            if count == 3:
                answer = "." + answer
                count = 0
            answer = char + answer
            count += 1
        return answer
# @lc code=end
