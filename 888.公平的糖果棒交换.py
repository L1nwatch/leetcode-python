#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果棒交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        set_a = set(aliceSizes)
        set_b = set(bobSizes)
        delta = (sum_a-sum_b)//2
        for num_b in set_b:
            if num_b+delta in set_a:
                return [num_b+delta, num_b]


# @lc code=end
