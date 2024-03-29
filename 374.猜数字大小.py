#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            middle = low + (high-low)//2
            guess_result = guess(middle)
            if guess_result == 0:
                return middle
            elif guess_result == 1:
                low = middle + 1
            elif guess_result == -1:
                high = middle
        return low
# @lc code=end
