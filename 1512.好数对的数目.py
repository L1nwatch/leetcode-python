#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def comb(self, n, m):
        import math
        return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        from collections import Counter
        counter = Counter(nums)
        for count in counter.values():
            if count > 1:
                answer += self.comb(count, 2)
        return answer
# @lc code=end
