#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        answer = list()
        nums.sort()
        sum_nums = sum(nums)
        while len(nums) > 0:
            num = nums.pop()
            answer.append(num)
            if 2 * sum(answer) > sum_nums:
                break
        return sorted(answer, reverse=True)
# @lc code=end
