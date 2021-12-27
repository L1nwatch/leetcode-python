#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = list()
        while len(nums) > 0:
            count = nums.pop(0)
            value = nums.pop(0)
            answer.extend([value]*count)
        return answer
# @lc code=end
