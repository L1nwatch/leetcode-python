#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = list()
        for i in range(n):
            answer.extend(nums[i::n])
        return answer
# @lc code=end

