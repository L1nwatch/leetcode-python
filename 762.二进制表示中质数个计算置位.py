#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        answer = 0
        num_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
        for i in range(left, right+1):
            reset_flag = bin(i).count("1")
            if reset_flag in num_set:
                answer += 1
        if left <= 1 <= right+1:
            answer -= 1
        return answer

# @lc code=end
