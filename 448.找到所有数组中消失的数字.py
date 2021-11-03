#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = set([i for i in range(1, len(nums)+1)])
        for each_num in nums:
            if each_num in result:
                result.remove(each_num)
        return list(result)
# @lc code=end
