#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        import collections
        counter = collections.Counter(nums)
        for key,value in counter.items():
            if value == n:
                return key
        return False
# @lc code=end

