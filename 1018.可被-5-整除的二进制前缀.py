#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = str()
        answer = list()
        for bit in nums:
            num += str(bit)
            answer.append(int(num, 2) % 5 == 0)
        return answer

# @lc code=end
