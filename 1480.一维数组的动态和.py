#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = list()
        sum_step = 0
        for num in nums:
            sum_step += num
            answer.append(sum_step)
        return answer
# @lc code=end

