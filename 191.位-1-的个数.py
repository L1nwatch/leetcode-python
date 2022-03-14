#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for each_char in bin(n)[2:]:
            if each_char == "1":
                count += 1
        return count
# @lc code=end


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for i in range(32) if n & (1 << i))

class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            n &= n-1
            answer += 1
        return answer

class Solution3:
    def hammingWeight(self, n: int) -> int:
        return sum([1 & (n >> 31-i) for i in range(32)])