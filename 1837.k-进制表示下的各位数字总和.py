#
# @lc app=leetcode.cn id=1837 lang=python3
#
# [1837] K 进制表示下的各位数字总和
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        answer = 0
        while n:
            answer += n % k
            n //= k
        return answer
# @lc code=end

