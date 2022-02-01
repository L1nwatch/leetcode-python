#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        answer = [0,0]
        for l,w in rectangles:
            k = min(l,w)
            if k > answer[0]:
                answer = [k,1]
            elif k == answer[0]:
                answer[1] += 1
        return answer[1]

# @lc code=end

