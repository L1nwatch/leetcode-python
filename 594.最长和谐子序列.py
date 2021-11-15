#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        answer = 0
        from collections import Counter
        count = Counter(nums)
        for each_key in count.keys():
            if each_key + 1 in count:
                answer = max(answer,count[each_key]+count[each_key+1])
        return answer
# @lc code=end
