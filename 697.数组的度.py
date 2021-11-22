#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        import collections
        count = collections.Counter(nums)
        max_count = max(list(count.values()))
        length_list = list()
        length = len(nums)
        for each_key, each_value in count.items():
            if each_value == max_count:
                length_list.append(length -
                                   nums[::-1].index(each_key) - nums.index(each_key))
        return min(length_list)
# @lc code=end
