#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        answer = 0
        money = 0
        for i in range(n):
            if i % 7 == 0:
                money += 1
                answer += money
            else:
                answer += money + i % 7
        return answer
# @lc code=end

