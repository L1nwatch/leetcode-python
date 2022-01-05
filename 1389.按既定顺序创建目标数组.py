#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = list()
        for i in range(len(nums)):
            answer.insert(index[i], nums[i])
        return answer
# @lc code=end
