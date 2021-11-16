#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                n -= 1
                i += 2
            else:
                i += 3
        return n <= 0
# @lc code=end

