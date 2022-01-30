#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n > 1:
            answer += n // 2
            if n % 2 == 0:
                n //= 2
            else:
                n = n //2 + 1
        return answer
# @lc code=end

