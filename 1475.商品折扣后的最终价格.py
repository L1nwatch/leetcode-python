#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = list()
        length = len(prices)
        for i in range(length):
            for j in range(i+1, length):
                if prices[j] <= prices[i]:
                    answer.append(prices[i]-prices[j])
                    break
            else:
                answer.append(prices[i])
        return answer
# @lc code=end
