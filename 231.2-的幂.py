#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
# @lc code=end
        if n < 0:
            return False
        elif n == 0:
            return False
        elif n == 1:
            return True
        elif n == 2:
            return True
        while n > 2:
            n = n / 2
            if n != 1 and n != 2 and n % 2 != 0:
                return False
        return True

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        for i in range(32):
            if num == n:
                return True
            elif num > n:
                return False
            num = num << 1
        return False

class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ( n & (n-1) ) == 0