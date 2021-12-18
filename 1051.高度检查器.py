#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        right_heights = sorted(heights)
        for height,right_height in zip(heights,right_heights):
            if height != right_height:
                answer += 1
        return answer

# @lc code=end

