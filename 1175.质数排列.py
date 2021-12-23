#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
class Solution:
    def get_prime_count(self, n: int) -> int:
        answer = 0
        for i in range(2, n+1):
            for j in range(2, i//2+1):
                if i % j == 0:
                    break
            else:
                answer += 1
        return answer

    def numPrimeArrangements(self, n: int) -> int:
        prime_count = self.get_prime_count(n)
        not_prime_count = n-prime_count
        answer = 1
        mod = 10**9+7
        for i in range(2, prime_count+1):
            answer = answer * i % mod
        for i in range(2, not_prime_count+1):
            answer = answer * i % mod
        return answer
# @lc code=end
