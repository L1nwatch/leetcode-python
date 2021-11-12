#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        result = set()
        for i in range(len(candyType)):
            if len(result) >= len(candyType)/2:
                break

            if candyType[i] not in result:
                result.add(candyType[i])
        return len(result)
# @lc code=end
