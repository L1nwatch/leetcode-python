#
# @lc app=leetcode.cn id=1848 lang=python3
#
# [1848] 到目标元素的最小距离
#

# @lc code=start
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = len(nums)
        for i,num in enumerate(nums):
            if abs(i-start) > answer:
                break
            if num == target:
                answer = abs(i-start)
        return answer
# @lc code=end

