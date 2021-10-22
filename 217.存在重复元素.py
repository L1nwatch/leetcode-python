#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = dict()
        for each_data in nums:
            count[each_data] = count.get(each_data, 0) + 1
        for each_value in count.values():
            if each_value > 1:
                return True
        return False
# @lc code=end
