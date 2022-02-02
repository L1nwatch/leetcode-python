#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        answer = 0
        for num,value in counter.items():
            if value == 1:
                answer += num
        return answer
# @lc code=end

